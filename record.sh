WINDOW_ID=$(xwininfo | grep 'Window id' | awk '{print $4}')
recordmydesktop --windowid "$WINDOW_ID"
