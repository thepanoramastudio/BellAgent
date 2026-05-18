#!/bin/bash
MESSAGE=${1:-"update"}
cd "$(dirname "$0")"
git add .
git commit -m "$MESSAGE"
git push
echo ""
echo "Done! Now run in Cloud Shell:"
echo "  cd BellAgent && git pull && gcloud run deploy line-ai-customer-support-agent --source . --region us-west1 --allow-unauthenticated"
