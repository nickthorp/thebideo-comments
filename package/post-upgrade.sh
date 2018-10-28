#!/usr/bin/env bash

# Copy service files into approp dirs
cp -rf /opt/thebideo-comments/etc/* /etc/

systemctl daemon-reload

systemctl enable thebideo-comments.service

systemctl restart thebideo-comments