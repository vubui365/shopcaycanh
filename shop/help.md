# Các phần mềm cần thiết trong khóa học
1. Editor: Visual Studio Code : https://zendvn.com/bai-viet/huong-dan-su-dung-visual-studio-code-a-z-toan-tap-10
2. Python 3.11.3 ->
3. Xampp 8.2.4 ->
# Các extension visual studio code
1. Python (Microsoft)
2. Django
3. Material Icon Theme
# Lưu ý
- Nên sử dụng editor giống mình để học hiệu quả hơn.
- Nên sử dụng 1 profile chrome riêng để học.
- Tránh cài nhiều extension vào profile đó.

# Tip fix bug nhanh
- Nhớ bật Xampp, start Apache và start MySQL mỗi khi mở máy lên học.
- Xem kỹ từng dấu, ký tự đặc biệt và cả khoảng trắng trong video khi code theo nhưng gặp lỗi.
- Khi code bị lỗi thì có thể download phần mã nguồn tại video để tham khảo.
- Search google trước khi hỏi sẽ giúp tăng khả năng nghiêng cứu, giải quyết vấn đề, hình thành thói quen tự lực.
- Nếu có tự thay đổi gì ở phần css, js của template thì phải xóa cache trình duyệt đi rồi refresh trang web lại để xem sự thay đổi (học tới phần có giao diện web tin tức, bán hàng thì lưu ý).

# Module
1. Việc phân chia module dựa vào nhiều yếu tố
   1. Chức năng
   2. Nhân lực xây dựng
   3. Nhóm người dùng (Phân quyền)
   4. Phong cách code của DEV
2. Phân chia module trong project tin tức
   1. Quản lý category
   2. Quản lý article
   3. Quản lý feed
3. Giải pháp
   1. 3 module: category - article - feed
   2. 2 module: news - feeds
   3. 2 module: admin - publish
   4. 1 module: news
# Khám phá Django
- Link Document 4.2: https://docs.djangoproject.com/en/4.2/
- Xem version Django: django-admin startproject mysite
- Tạo project mới: django-admin startproject mysite
- Chạy server: python manage.py runserver
- Đổi port: python manage.py runserver 6969
- Tạo app mới: python manage.py startapp polls
- Tạo mới, áp dụng sự thay đổi cho cơ sở dữ liệu: python manage.py migrate
- Tạo user mới: python manage.py createsuperuser
# Áp dụng MySQL
- Tạo database mới tại phpmyadmin
- Config database tại settings.py
- Chạy lệnh python manage.py migrate
# Xây dựng quản lý Category - Thêm Sửa Xóa Đọc - CRUD
- Tạo Category, khai báo các trường tại models.py
- Khai báo app news tại INSTALLED_APP trong settings.py
- python manage.py makemigrations news
- python manage.py migrate
- Thiết lập phần hiển thị cho Category tại admin.py
- Tạo slug từ động từ name
- Tạo đường dẫn static file cho project
- Chạy file Javascript tại trang Admin Django
- Filter: Status, Is Homepage, Layout
- Search: Name
# Xây dựng quản lý Article - Thêm Sửa Xóa Đọc - CRUD
- Link Editor Content: https://pypi.org/project/django-tinymce
- Upload path: https://www.geeksforgeeks.org/python-uploading-images-in-django
- Random name image: https://stackoverflow.com/questions/2673647/enforce-unique-upload-file-names-using-django
- Delete image: https://stackoverflow.com/questions/2878490/how-to-delete-old-image-when-update-imagefield

# Xây dựng quản lý Feed - Thêm Sửa Xóa Đọc - CRUD

# Nhúng và tối ưu giao diện cho backend
- Tải và giải nén giao diện template_news tại phần mã nguồn của video
- Xây dựng các thành phần dùng chung (hạn chế lặp lại các thành phần HTML)
- Tạo layout và dùng block content
- Xây dựng các layout con (multi layout)

# Xây dựng trang hiển thị bài viết của mỗi Category
- Dùng get_object_or_404 để tìm dữ liệu trong database (trả về lỗi 404 khi không tìm thấy).
- Lọc bài viết theo category, status và publish_date (filter).
- Sắp xếp bài viết mới nhất trước (order).
- Phân trang bằng Paginator.
- Render html và truyền ra biến dữ liệu để sử dụng tại template.
- Sử dụng các cú pháp đổ dữ liệu, thực hiện câu lệnh if else for tại template django.
- Hàm format ngày tháng, rút gọn nội dung bài viết, đổ html (date, truncatechars, safe).

# Xây dựng trang hiển thị nội dung bài viết
- Loại bỏ bài viết hiện tại trong bài viết liên quan bằng exclude.
- Định nghĩa hàm get_absolute_url, tối ưu việc thay thế đường dẫn.

# Xây dựng trang chủ cho trang tin tức
- Dùng hàm slice để giới hạn lượng bài viết được đổ ra tại django template.

# Xây dựng chức năng tìm kiếm và trang hiển thị kết quả
- Tự tạo 1 template tag sử dụng tại django template.
- Một số lookup dùng để tìm kiếm:
1. contains: Tìm kiếm các giá trị có chứa một chuỗi con cụ thể.
2. icontains: Tìm kiếm các giá trị có chứa một chuỗi con cụ thể (không phân biệt chữ hoa/chữ thường).
3. regex: Tìm kiếm các giá trị phù hợp với một biểu thức chính quy cụ thể.
4. iregex: Tìm kiếm các giá trị phù hợp với một biểu thức chính quy cụ thể (không phân biệt chữ hoa/chữ thường).

# Xây dựng trang tin tức tổng hợp từ nguồn cấp bên ngoài
- Lấy và chuyển dữ liệu rss sang json để xử lý
- Cách ghi json ra 1 file, xử lý trường hợp bị mã hóa nội dung
- Sử dụng Beautiful Soup lấy src image

# Xây dựng các context khởi chạy mặc định
- Category: Menu, Sidebar
- Feed: Menu, Sidebar
- Bài viết gần đây: Sidebar
- Bài viết ngẫu nhiên: Footer

# Xây dựng chức năng hiển thị giá vàng, giá coin
- Link Document API: http://apiforlearning.zendvn.com
- Get Coin: http://apiforlearning.zendvn.com/api/get-coin
- Get Gold: http://apiforlearning.zendvn.com/api/get-gold

# URL Friendly
- Dạng url mới, các website hay sử dụng
- Thân thiện với Google, SEO
- Học thêm biểu thức chính quy: https://www.youtube.com/playlist?list=PLv6GftO355AsBwDpVLeo-lJWPEba1Qso8

# Các đoạn regular expression
- re_path(r'^(?P<article_slug>[\w-]+)-a(?P<article_id>\d+)\.html$', views.article, name='article'),
- re_path(r'^tin-tuc-tong-hop-(?P<feed_slug>[\w-]+)\.html$', views.feed, name='feed'),
- re.search(r'^(?P<article_slug>[\w-]+)-a\d+\.html$', last_path)

# Tối ưu hơn nữa
- Tách model ra thành nhiều file riêng, xử lý lỗi import model ở các file khác.
- Tạo template tag render chung 1 template (dành cho những chỗ có cấu trúc html giống nhau)

# Xây dựng website bán hàng (bán cây cảnh)

- Đất Nền
- Thủy Sinh

Product N - N Planting Method

# Xây dựng các phần quản lý cho website bán hàng
- Tiếp cận cách xử lý tình huống với mối quan hệ nhiều nhiều giữa các bảng.
- null=True, blank=True (Đối với các trường được phép rỗng hoặc để trống)
- editable=False (Đối với các trường không cho edit hoặc người quản trị tự điền)
- Xử lý lấy price_real khi người dùng lưu sản phẩm (cách định nghĩa lại phương thức save)
- Cách format dữ liệu các trường hiển thị tại admin, đặt tên lại cho các trường dữ liệu.
- Phân biệt giữa fields, readonly_fields, list_display.
- Cách không cho phép thêm mới từ phần quản trị.

# Đẩy phần xử lý active menu, danh mục, sắp xếp,... về phía client
active phía server: 10 người dùng => gửi yêu cầu => kiểm tra điều kiện để active 10 lần => html, css, js
         1000 người => gửi yêu cầu => kiểm tra điều kiện để active 1000 lần => html, css, js

active phía client: 10 người dùng => gửi yêu cầu => html, css, js => active về phía client

- Vừa giúp code trong backend chúng ta nó gọn hơn
- Vừa giảm tải được cho hệ thống

# Update Cart
1. Trừ: /cap-nhat-gio-hang.html?productId=37&action=decrease
- TH1: Số lượng của sản phẩm lớn hơn 1
- TH2: Số lượng của sản phẩm bằng hoặc bé hơn 1

2. Cộng: /cap-nhat-gio-hang.html?productId=37&action=increase

3. Xóa: /cap-nhat-gio-hang.html?productId=37&action=delete

# Gửi mail django thông qua Gmail server
1. Chuẩn Bị
- Có tài khoản gmail và đăng nhập sẵn trên trình duyệt
- Vào trang quản lý tài khoản Google: https://myaccount.google.com
- Bật xác thực 2 bước
- Lấy mật khẩu ứng dụng
2. Thực hiện gửi mail từ django project
- Cài đặt: pip install django-smtp-ssl

# Deloy Project: Đẩy website Django lên internet
- Server, VPS, Hosting, Domain...
1. Mục đích:
- Làm quen với việc publish sản phẩm từ local lên server.
- Hiểu được cách chạy một sản phẩm ngoài thực tế phải thông qua những công cụ gì.
- Có link sản phẩm để demo trong CV ứng tuyển việc làm.
2. Các bước thực hiện:
- Cài đặt git: https://git-scm.com
- Tạo tài khoản github: https://github.com/signup
- Tạo repository trên github
- git init
- git add .
- git commit -m "first commit"
- Tạo personal access token trên github setting
- Thay token, username và repo vào: git remote set-url origin https://<username>:<personal-access-token>@github.com/<user>/<your-repo>.git
- Ví dụ: git remote set-url origin https://vuongquydev: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@github.com/vuongquydev/django.git
- git push -u origin main
- Đăng nhập github tại máy
- Đẩy sourcecode lên github
- Tạo account gói miễn phí tại: https://www.pythonanywhere.com
- Tiến hành các bước publish website theo video
- Tạo cơ sở dữ liệu và mật khẩu csdl
- Kéo source code từ git về: git clone <your-repository>
- Nhập username và token github
- Tạo app mới
- Cấu hình tại settings.py và một số chỗ theo video
- Import dữ liệu: source /home/<your-username>/<your-sql-file>.sql
- pip install pymysql
- pip install django-tinymce
- pip install django-cleanup
- pwd để xem thư mục mình đang ở
- Chạy và tìm các file static: cd django => python manage.py collectstatic
- Cấu hình lại static folder
- Nhớ reload lại app mỗi khi thay đổi bất cứ thứ gì

# Các câu lệnh thường dùng
- python manage.py runserver
- python manage.py makemigrations
- python manage.py migrate

- Client - Khách Truy Cập
- Admin - Phía Quản Lý

