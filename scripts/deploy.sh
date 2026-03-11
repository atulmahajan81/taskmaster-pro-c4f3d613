#!/bin/bash

# Pull latest changes
ssh $DEPLOY_USER@$SERVER 'cd /path/to/app && git pull'

# Build and restart
ssh $DEPLOY_USER@$SERVER 'cd /path/to/app && docker-compose -f docker-compose.yml -f docker-compose.prod.yml build && docker-compose up -d'