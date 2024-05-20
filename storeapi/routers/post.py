from storeapi.models.post import UserPostIn, CommentIn
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


post_table = {}
comment_table = {}


def find_post_by_id(post_id: int):
    return post_table.get(post_id)


@router.post("/post")
async def create_post(post: UserPostIn, status_code=201):
    data = post.model_dump()
    last_record_id = len(post_table)
    new_post = {**data, "id": last_record_id}
    post_table[last_record_id] = new_post
    return new_post


@router.post("/comment")
async def create_comment(comment: CommentIn, status_code=201):
    post = find_post_by_id(comment.post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    data = comment.model_dump()
    last_record_id = len(comment_table)
    new_comment = {**data, "id": last_record_id}
    comment_table[last_record_id] = new_comment
    return new_comment


@router.get("/post")
async def get_post():
    return post_table


@router.get("/comment")
async def get_comment():
    return comment_table


@router.get("/post/{post_id}/comments")
async def get_post_comments(post_id: int):
    post = find_post_by_id(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    comments = [comment for comment in comment_table.values() if comment["post_id"] == post_id]
    return comments


@router.get("/post/{post_id}")
async def get_post(post_id: int):
    post = find_post_by_id(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
