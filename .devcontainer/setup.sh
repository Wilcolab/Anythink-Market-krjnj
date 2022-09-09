# Update engine that codespace started for user
WILCO_ID="`cat .wilco`"
ENGINE_EVENT_ENDPOINT="${ENGINE_BASE_URL}/users/${WILCO_ID}/event"

curl -L -X POST "$ENGINE_EVENT_ENDPOINT" -H "Content-Type: application/json" --data-raw "{ \"event\": \"github_codespace_started\" }"

# Export backend url when in codespaces
echo "export CODESPACE_BACKEND_URL=\"https://${CODESPACE_NAME}-3000.githubpreview.dev\"" >> ~/.bashrc

# Change backend port visibility to public
echo "(&>/dev/null .devcontainer/open_port.sh &)" >> ~/.bashrc
