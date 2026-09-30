from typing import Any, Optional

from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    ConfigDict,
)


class RegisterRequest(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=120,
    )

    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=128,
    )


class LoginRequest(BaseModel):
    email: EmailStr

    password: str = Field(
        min_length=1,
        max_length=128,
    )


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class HomeItem(BaseModel):
    category: str = Field(
        min_length=1,
        max_length=80,
    )

    quantity: int = Field(
        default=1,
        ge=1,
        le=100,
    )


class HomeRequest(BaseModel):
    budget: float = Field(
        gt=0,
        le=10_000_000,
    )

    currency: str = Field(
        default="INR",
        max_length=8,
    )

    room_type: str = Field(
        min_length=2,
        max_length=80,
    )

    style: str = Field(
        default="modern",
        max_length=80,
    )

    items: list[HomeItem] = Field(
        min_length=1,
        max_length=20,
    )

    notes: Optional[str] = Field(
        default="",
        max_length=1000,
    )


class PartyRequest(BaseModel):
    budget: float = Field(
        gt=0,
        le=10_000_000,
    )

    currency: str = Field(
        default="INR",
        max_length=8,
    )

    event_type: str = Field(
        min_length=2,
        max_length=80,
    )

    guests: int = Field(
        ge=1,
        le=10000,
    )

    venue: str = Field(
        default="Home / flexible",
        max_length=120,
    )

    city: str = Field(
        default="",
        max_length=120,
    )

    food_preference: str = Field(
        default="Mixed",
        max_length=80,
    )

    notes: Optional[str] = Field(
        default="",
        max_length=1000,
    )


class RecommendationItem(BaseModel):
    name: str

    category: str

    platform: str

    estimated_price: float = Field(
        ge=0
    )

    quantity: int = Field(
        default=1,
        ge=1,
    )

    reason: str

    url: str


class RecommendationResponse(BaseModel):
    planner: str

    budget: float

    estimated_total: float

    remaining_budget: float

    budget_allocation: dict[str, float] = {}

    summary: str

    recommendations: list[RecommendationItem]

    source: str

    warnings: list[str] = []


class HistoryResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    planner: str

    budget: str

    created_at: Any