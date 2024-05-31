from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class ImageProducts(BaseModel):
    id_product: Optional[str]  # Foreign key to Product
    url_image: Optional[str]

class ImportInvoiceDetails(BaseModel):
    id_import_invoice: Optional[str]  # Foreign key to ImportInvoice
    id_product: Optional[str]  # Foreign key to Product
    quantity: Optional[int]
    import_price: Optional[float]
    total_price: Optional[float]

class SellInvoiceDetails(BaseModel):
    id_sell_invoice: Optional[str]  # Foreign key to SellInvoice
    id_product: Optional[str]  # Foreign key to Product
    quantity: Optional[int]
    sell_price: Optional[float]
    toltal_price: Optional[float]


class Products(BaseModel):
    id_category: Optional[str]  # Foreign key to Category
    id_category_offer: Optional[str]  # Foreign key to CategoryOffer
    id_manufactor: Optional[str]  # Foreign key to Manufacter
    name_product: Optional[str]
    url_image: Optional[str]
    origin: Optional[str]
    rate: Optional[float]
    description: Optional[str]
    detail_description: Optional[str]

class ProductDetails(BaseModel):
    id_product: Optional[str]  # Foreign key to Product
    price: Optional[float]
    price_sales: Optional[float]
    quantity: Optional[int]
    status: Optional[bool]
    view: Optional[int]
    weight: Optional[str]
    view_sales: Optional[int]

class AccountDetails(BaseModel):
    id_account: Optional[str]  # Foreign key to Account
    id_type_account: Optional[str]  # Foreign key to TypeAccount
    fullname: Optional[str]
    address: Optional[str]
    phone: Optional[str]
    url_image: Optional[str]

class Rates(BaseModel):
    id_product: Optional[str]  # Foreign key to Product
    id_account: Optional[str]  # Foreign key to Account
    quantity: Optional[float]
    rate_content: Optional[str]
    status: Optional[bool]
    time: Optional[datetime] = Field(default_factory=datetime.now)
    rate_image: Optional[str]
    note: Optional[str]

class Categorys(BaseModel):
    category_name: Optional[str]
    status: Optional[bool]
    content_category: Optional[str]

class CategoryOffers(BaseModel):
    category_offer_name: Optional[str]
    status: Optional[bool]
    content_category_offer: Optional[str]

class Manufactors(BaseModel):
    name_manufactor: Optional[str]
    link_web: Optional[str]
    url_image: Optional[str]

class ImportInvoices(BaseModel):
    id_distributor: Optional[str]  # Foreign key to Distributor
    time: Optional[datetime] = Field(default_factory=datetime.now)
    payment_type: Optional[str]
    id_account: Optional[str]  # Foreign key to TaiKhoan
    toltal_price: Optional[float]

class SellInvoices(BaseModel):
    name_customer: Optional[str]
    address: Optional[str]
    address_detail: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    time: Optional[datetime] = Field(default_factory=datetime.now)
    toltal_price: Optional[float]
    id_account: Optional[str]  # Foreign key to Account
    status_invoice: Optional[str]

class TypeAccounts(BaseModel):
    name_type_account: Optional[str]
    description: Optional[str]

class Distributors(BaseModel):
    name_distributor: Optional[str]
    address: Optional[str]
    phone: Optional[str]
    description: Optional[str]
    linkweb: Optional[str]

class Advertisments(BaseModel):
    url_image: Optional[str]
    url_web: Optional[str]
    description: Optional[str]

class Slides(BaseModel):
    title: Optional[str]
    description: Optional[str]
    url_image: Optional[str]

class Accounts(BaseModel):
    name_account: Optional[str]
    password: Optional[str]
    email: Optional[str]

class News(BaseModel):
    title: Optional[str]
    new_content: Optional[str]
    url_image: Optional[str]
    id_account: Optional[str]  # Foreign key to Account
    new_view: Optional[int]
    new_status: Optional[str]

