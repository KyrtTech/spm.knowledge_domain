#!/bin/bash

. ./.env

jq -cr 'to_entries[] | (.key) + "=" + .value' map.json | while read i; do
    files=(${i//=/ })
    echo "Copying ${files[0]} to s3://${AWS_S3_BUCKET}/${files[1]}"
    aws s3 cp ../ontology/${files[0]} s3://${AWS_S3_BUCKET}/${files[1]} --profile=${AWS_PROFILE}
done

echo "Invalidating CDN"
aws cloudfront create-invalidation --distribution-id ${CLOUDFRONT_DISTRIBUTION_ID} --paths "/*" --profile=${AWS_PROFILE}
