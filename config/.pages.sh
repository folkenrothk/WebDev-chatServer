#!/usr/bin/bash
export PAGES_URL=$(curl -sb -H "Accept:application/json" -u dluman:$GWIZ_TOKEN $GITHUB_API_URL/repos/$GITHUB_REPOSITORY/pages)
