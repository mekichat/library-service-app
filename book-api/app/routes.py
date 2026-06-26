from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Book
from app.schemas import BookCreate, BookUpdate, BookResponse

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


@router.get(
    "/",
    response_model=list[BookResponse],
    summary="Get all books",
    description="Returns a list of all available books in the system.",
    tags=["Books"]
)
def get_books():

    db: Session = SessionLocal()

    books = db.query(Book).all()
    
    db.close()

    return books


@router.get(
    "/{id}",
    response_model=BookResponse,
    summary="Get book by ID",
    description="Fetch a single book using its unique ID.",
    tags=["Books"]
)
def get_book(id: int):

    db: Session = SessionLocal()

    book = db.get(Book, id)

    db.close()
    
    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return book


@router.post(
    "/",
    response_model=BookResponse,
    summary="Create a new book",
    description="Adds a new book into the database.",
    tags=["Books"]
)
def create_book(book: BookCreate):

    db: Session = SessionLocal()

    db_book = Book(
        title=book.title,
        author=book.author,
        price=book.price,
    )

    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    db.close()

    return db_book

@router.put(
    "/{id}",
    response_model=BookResponse,
    summary="Update a book",
    description="Updates an existing book by ID.",
    tags=["Books"]
)
def update_book(id: int, updated_book: BookUpdate):

    db: Session = SessionLocal()

    book = db.get(Book, id)

    if book is None:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    book.title = updated_book.title
    book.author = updated_book.author
    book.price = updated_book.price

    db.commit()
    db.refresh(book)

    db.close()

    return book

@router.delete(
    "/{id}",
    summary="Delete a book",
    description="Removes a book permanently from the database.",
    tags=["Books"]
)
def delete_book(id: int):

    db: Session = SessionLocal()
    
    book = db.get(Book, id)
    
    if book is None:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    db.delete(book)

    db.commit()

    return {"status":"deleted"}