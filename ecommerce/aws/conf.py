import datetime

AWS_GROUP_NAME = "ax_ecommerce_group"
AWS_USERNAME = "ax-ecommerce-user"
AWS_ACCESS_KEY_ID = "AKIAJZB4E2ORGPOX52HQ"
AWS_SECRET_ACCESS_KEY = "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"
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True

DEFAULT_FILE_STORAGE = 'ecommerce.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'ecommerce.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'ax-ecommerce'
S3DIRECT_REGION = 'us-west-2'
# S3_USE_SIGV4 = True
# AWS_S3_SIGNATURE_VERSION = 's3v4'
# S3_URL = '//s3.us-east-2.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
# MEDIA_URL = '//s3.us-east-2.amazonaws.com/media/%s/' % AWS_STORAGE_BUCKET_NAME
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = {
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}

