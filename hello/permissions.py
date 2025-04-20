from rest_framework import permissions
from hello.models import Board, Workspace  # Import the Board and Workspace models

class IsWorkspaceMember(permissions.BasePermission):
    """
    Allows access only to members of the workspace.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        workspace_id = view.kwargs.get('workspace_id')
        if workspace_id is None:
            return True
        try:
            workspace = Workspace.objects.get(pk=workspace_id)
            return request.user in workspace.members.all()
        except Workspace.DoesNotExist:
            return False

class IsBoardWorkspaceMember(permissions.BasePermission):
    """
    Allows access only to members of the workspace that the board belongs to.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        board_id = view.kwargs.get('board_id')
        if board_id is None:
            return True
        try:
            board = Board.objects.get(pk=board_id)
            return request.user in board.workspace.members.all()
        except Board.DoesNotExist:
            return False
