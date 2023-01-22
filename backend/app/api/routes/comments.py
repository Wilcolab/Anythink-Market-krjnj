from typing import Optional

from fastapi import APIRouter, Body, Depends, Response
from starlette import status

from app.api.dependencies.items import get_item_by_slug_from_path
from app.api.dependencies.authentication import get_current_user_authorizer
from app.api.dependencies.comments import (
    check_comment_modification_permissions,
    get_comment_by_id_from_path,
)
from app.api.dependencies.database import get_repository
from app.db.repositories.comments import CommentsRepository
from app.models.domain.items import Item
from app.models.domain.comments import Comment
from app.models.domain.users import User
from app.models.schemas.comments import (
    CommentInCreate,
    CommentInResponse,
    ListOfCommentsInResponse,
)

router = APIRouter()


@router.get(
    "",
    response_model=ListOfCommentsInResponse,
    name="comments:get-comments-for-item",
)
async def list_comments_for_item(
    item: Item = Depends(get_item_by_slug_from_path),
    user: Optional[User] = Depends(get_current_user_authorizer(required=False)),
    comments_repo: CommentsRepository = Depends(get_repository(CommentsRepository)),
) -> ListOfCommentsInResponse:
    comments = await comments_repo.get_comments_for_item(item=item, user=user)
    return ListOfCommentsInResponse(comments=comments)


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=CommentInResponse,
    name="comments:create-comment-for-item",
)
async def create_comment_for_item(
    comment_create: CommentInCreate = Body(..., embed=True, alias="comment"),
    item: Item = Depends(get_item_by_slug_from_path),
    user: User = Depends(get_current_user_authorizer()),
    comments_repo: CommentsRepository = Depends(get_repository(CommentsRepository)),
) -> CommentInResponse:
    comment = await comments_repo.create_comment_for_item(
        body=comment_create.body,
        item=item,
        user=user,
    )
    return CommentInResponse(comment=comment)


@router.delete(
    "/{comment_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    name="comments:delete-comment-from-item",
    dependencies=[Depends(check_comment_modification_permissions)],
    response_class=Response,
)
async def delete_comment_from_item(
    comment: Comment = Depends(get_comment_by_id_from_path),
    comments_repo: CommentsRepository = Depends(get_repository(CommentsRepository)),
) -> None:
    await comments_repo.delete_comment(comment=comment)
