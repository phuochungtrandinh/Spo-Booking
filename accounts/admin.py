from django.contrib import admin
from django.utils.html import format_html

from .models import Users


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    """
    Trang 'Quản lý khách hàng' trong Django Admin
    """

    list_display = (
        "full_name",       # hoặc 'name' / 'customer_name' tùy bạn đặt
        "email",
        "phone",    # nếu bạn dùng tên khác, sửa lại
        "role",
        "booking_count",   # cột số lần đặt (nếu chưa có thì giữ nguyên 0)
        "last_booking",    # cột lần đặt cuối (mockup có)
        "status_badge",    # cột Trạng thái (pill màu xanh / xám)
    )

    list_display_links = ("full_name",)  # click vào tên để vào chi tiết
    search_fields = ("full_name", "email", "phone")
    list_filter = ("role", "is_active", "is_deleted")
    ordering = ("full_name",)
    list_per_page = 20
    change_list_template = "admin/change_list.html"
    change_list_results_template = "admin/change_list_results.html"


    def booking_count(self, obj):
        """
        Số lần đặt (mockup là '15 lần', '8 lần'…).
        Tạm thời mình trả về 0 lần, bạn có thể sửa lại
        để count thật từ model Bookings nếu muốn.
        """
        return "0 lần"

    booking_count.short_description = "Số lần đặt"

    def last_booking(self, obj):
        """
        Lần đặt cuối (mockup có ngày).
        Nếu bạn có field datetime nào đó (vd: last_booking_at)
        thì đổi chỗ này cho đúng.
        """
        return "-"
    last_booking.short_description = "Lần đặt cuối"

    def status_badge(self, obj):
        """
        Hiển thị pill trạng thái giống mockup:
        - Đang hoạt động (màu xanh)
        - Không hoạt động (màu xám)
        Dựa trên is_active hoặc is_deleted.
        """
        if getattr(obj, "is_active", False) and not getattr(obj, "is_deleted", False):
            css_class = "status-pill status-active"
            text = "Đang hoạt động"
        else:
            css_class = "status-pill status-inactive"
            text = "Không hoạt động"

        return format_html('<span class="{}">{}</span>', css_class, text)

    status_badge.short_description = "Trạng thái"
    status_badge.allow_tags = True

