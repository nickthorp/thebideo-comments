#!/usr/bin/env bash

systemctl stop thebideo-comments
systemctl disable thebideo-comments.service
systemctl daemon-reload

# Copy service files into approp dirs
rm -f /etc/systemd/system/thebideo-comments.service
