from django.urls import path
from .views import (
    DashboardView, 
    AssetListView, 
    AssetCreateView, 
    SignUpView, 
    AssetUpdateView,
    AssetDeleteView,
    AssetHistoryView, 
    AssetRevertView,
    AssetDetailView,
    AddMaintenanceLogView,
    export_assets_csv,
)

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('list/', AssetListView.as_view(), name='asset-list'),
    path('create/', AssetCreateView.as_view(), name='asset-create'),
    path('update/<int:pk>/', AssetUpdateView.as_view(), name='asset-update'),
    path('delete/<int:pk>/', AssetDeleteView.as_view(), name='asset-delete'),
    path('register/', SignUpView.as_view(), name='register'),
    path('<int:pk>/history/', AssetHistoryView.as_view(), name='asset-history'),
    path('<int:pk>/history/<int:history_id>/revert/', AssetRevertView.as_view(), name='asset-revert'),
    # Part 2: Asset Detail & Maintenance Log
    path('<int:pk>/detail/', AssetDetailView.as_view(), name='asset-detail'),
    path('<int:pk>/maintenance/add/', AddMaintenanceLogView.as_view(), name='add-maintenance-log'),
    # Part 3: CSV Export
    path('export/csv/', export_assets_csv, name='export-assets-csv'),
]