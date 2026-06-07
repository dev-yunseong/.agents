---
name: minio
description: Use this skill to upload files or static sites to the configured MinIO server at https://s3.yunseong.dev and return a public URL. Trigger when the user asks to upload, host, share, or send a file or site via MinIO, S3, or object storage.
metadata:
  short-description: Upload files to MinIO
---

# MinIO Upload Skill

Use this skill to upload files or static sites to MinIO at `https://s3.yunseong.dev` and share a public URL.

Invoke when user says "upload to minio", "share via minio", "send screenshot", "host this file", "put on s3", or similar.

## Alias

The `yunseong` alias should be pre-configured:
- URL: `https://s3.yunseong.dev`

If the alias is missing, configure it from local secrets instead of storing credentials in this skill:
```bash
mc alias set yunseong https://s3.yunseong.dev "$MINIO_ACCESS_KEY" "$MINIO_SECRET_KEY"
```

If the required environment variables are not available, ask the user for the preferred credential source.

## Default bucket: `agent-artifacts`

Always upload to `agent-artifacts` unless the user specifies otherwise.

```bash
# Upload a file
mc cp <local-path> yunseong/agent-artifacts/<object-name>
```

Public URL: `https://s3.yunseong.dev/agent-artifacts/<object-name>`

## Upload a static site directory

```bash
mc cp --recursive <local-dir>/ yunseong/agent-artifacts/
```

Access at: `https://s3.yunseong.dev/agent-artifacts/index.html`

## Notes

- `agent-artifacts` is already public (anonymous download set)
- `mc ls yunseong/agent-artifacts` to check contents
- `mc rm yunseong/agent-artifacts/<object>` to delete
