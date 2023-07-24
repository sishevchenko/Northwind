from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/login")
async def login():
    return "login"


@router.post("/logout")
async def logout():
    return "logout"


@router.post("/create")
async def create():
    return "create"


@router.post("/update")
async def update():
    return "update"


@router.post("/delete")
async def deactivate():
    return "deactivate"
