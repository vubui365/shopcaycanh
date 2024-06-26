APP_VALUE_STATUS_ACTIVE         = "published"
APP_VALUE_LAYOUT_DEFAULT        = "list"
APP_VALUE_STATUS_DEFAULT        = 'draft'
APP_VALUE_STATUS_ORDER_DEFAULT  = 'order'

APP_PATH_PAGES =  "shop/pages/"

APP_VALUE_IMAGE_DEFAULT = '/media/news/images/feed/no-image.png'

TABLE_PLANTING_METHOD_SHOW  = "Planting Method"
TABLE_CATEGORY_SHOW         = "Category"
TABLE_PRODUCT_SHOW          = "Product"
TABLE_CONTACT_SHOW          = "Contact"
TABLE_ORDER_SHOW            = "Order"

APP_VALUE_STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

APP_VALUE_LAYOUT_CHOICES = (
        ('list', 'List'),
        ('grid', 'Grid')
    )

APP_VALUE_STATUS_ORDER_CHOICES = (
        ('order', 'Order'),
        ('confirm', 'Confirm'),
        ('delivery', 'Delivery'),
        ('finish', 'Finish'),
    )

SETTING_PRODUCT_TOTAL_ITEMS_SPECIAL_INDEX   = 8
SETTING_PRODUCT_TOTAL_ITEMS_LATEST_INDEX    = 9
SETTING_PRODUCT_TOTAL_ITEMS_HOT_INDEX       = 9
SETTING_PRODUCT_TOTAL_ITEMS_RANDOM_INDEX    = 9
SETTING_PRODUCT_TOTAL_ITEMS_RELATED         = 6
SETTING_CATEGORY_TOTAL_ITEMS_SIDEBAR        = 6
SETTING_PLANTING_METHOD_TOTAL_ITEMS_SIDEBAR = 4
SETTING_PRODUCT_TOTAL_ITEMS_PER_PAGE        = 9
SETTING_PRODUCT_TOTAL_ITEMS_LATEST_SIDEBAR  = 9
SETTING_PRODUCT_TOTAL_ITEMS_PER_SLIDE       = 3
SETTING_CATEGORY_TOTAL_ITEMS_MENU           = 6


ADMIN_SRC_JS        = ('my_admin/js/jquery-3.6.0.min.js', 'my_admin/js/slugify.min.js', 'my_admin/js/general.js')

ADMIN_SRC_CSS       = {'all': ('my_admin/css/custom.css',)}
ADMIN_HEADER_NAME   = "ZendVN Administration"

ADMIN_EMAIL_RECEIVE = 'davidpham9793@gmail.com'


NOTIFY_ORDER_SUCCESS    = 'Cảm ơn bạn đã đặt hàng từ chúng tôi!'
NOTIFY_CONTACT_SUCCESS  = 'Cảm ơn bạn đã liên hệ với chúng tôi!'

NOTIFY_ORDER_CHECK_NOT_EXIST    = 'Không tìm thấy đơn hàng, vui lòng kiểm tra lại mã đơn!'
NOTIFY_ORDER_CHECK_NOT_NULL     = 'Vui lòng nhập mã đơn!'

NOTIFY_EMAIL_SUBJECT_CONTACT    = 'ZendVN - Thông báo liên hệ thành công'
NOTIFY_EMAIL_SUBJECT_ORDER      = "ZendVN - Thông báo đặt hàng thành công"