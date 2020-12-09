import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Customers(Base):
    __tablename__ = 'Customers'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(VARCHAR(length=50), nullable=False)
    TIN = Column(VARCHAR(length=10), nullable=False)
    CIO = Column(VARCHAR(length=9), nullable=False)
    MGRN = Column(VARCHAR(length=15), nullable=True)

class Clients(Base):
    __tablename__ = 'Clients'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    full_name = Column(VARCHAR(length=255), nullable=False)
    passport_data = Column(VARCHAR(length=12), nullable=False)
    phone_number = Column(VARCHAR(length=12), nullable=False)
    email = Column(VARCHAR(length=50), nullable=False)
    date_of_registration = Column(DATE, nullable=False)
    insurance_number = Column(VARCHAR(length=13), nullable=False)
    gender = Column(Boolean, nullable=False)
    foreign_passport_data = Column(VARCHAR(length=12), nullable=False)

    customers = relationship('Customers', backref='customers-clients')
    customer_id = Column(Integer, ForeignKey('Customers.id'), nullable=False)

class Partners(Base):
    __tablename__ = 'Partners'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(VARCHAR(length=100), nullable=False)
    type = Column(Integer, nullable=False)
    address = Column(VARCHAR(length=255), nullable=False)
    phone_number = Column(VARCHAR(length=12), nullable=False)

class Partners_contracts(Base):
    __tablename__ = 'Partners_contracts'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    partners = relationship('Partners', backref='partners-partners_contracts')
    partner_id = Column(Integer, ForeignKey('Partners.id'), nullable=False)

    name = Column(VARCHAR(length=100), nullable=False)
    date_of_contract_begin = Column(DATE, nullable=False)
    date_of_contract_end = Column(DATE, nullable=False)

class Tours(Base):
    __tablename__ = 'Tours'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(VARCHAR(length=255), nullable=False)
    description = Column(VARCHAR(length=1000), nullable=False)
    photo_url = Column(Text, nullable=False)
    amount = Column(DECIMAL(10,2), nullable=False)

class Tour_types(Base):
    __tablename__ = 'Tour_types'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(VARCHAR(length=100), nullable=False)
    description = Column(VARCHAR(length=1000), nullable=False)
    photo_url = Column(Text, nullable=False)

class Types_inside_tours(Base):
    __tablename__ = 'Types_inside_tours'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    tour_types = relationship('Tour_types', backref='tour_types-types_inside_tours')
    tour_type_id = Column(Integer, ForeignKey('Tour_types.id'), nullable=False)

    tours = relationship('Tours', backref='tours-types_inside_tours')
    tour_id = Column(Integer, ForeignKey('Tours.id'), nullable=False)

class Tour_services(Base):
    __tablename__ = 'Tour_services'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(VARCHAR(length=100), nullable=False)
    description = Column(VARCHAR(length=1000), nullable=False)
    required = Column(Boolean, nullable=False)

class Services_inside_tours(Base):
    __tablename__ = 'Services_inside_tours'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    tours = relationship('Tours', backref='tours-services_inside_tours')
    tour_id = Column(Integer, ForeignKey('Tours.id'), nullable=False)

    tour_services = relationship('Tour_services', backref='tour_services-services_inside_tours')
    tour_service_id = Column(Integer, ForeignKey('Tour_services.id'), nullable=False)

class Tour_requests(Base):
    __tablename__ = 'Tour_requests'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    clients = relationship('Clients', backref='clients-requests')
    client_id = Column(Integer, ForeignKey('Clients.id'))

    partners = relationship('Partners', backref='partners-requests')
    partner_id = Column(Integer, ForeignKey('Partners.id'), nullable=False)

    date_of_request = Column(DATE, nullable=False)
    price = Column(DECIMAL(10,2), nullable=False)
    status = Column(Integer, nullable=False)
    comment = Column(VARCHAR(length=1000), nullable=True)
    date_of_begin = Column(DATE, nullable=False)
    count_of_nights = Column(Integer, nullable=False)

    tours = relationship('Tours', backref='tours-tour_requests')
    tours_id = Column(Integer, ForeignKey('Tours.id'), nullable=False)

class Request_vouchers(Base):
    __tablename__ = 'Request_vouchers'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    tour_requests = relationship('Tour_request', backref='tour_requests-request_vouchers')
    tour_request_id = Column(Integer, ForeignKey('Tour_requests.id'), nullable=False)

    clients_contracts = relationship('Clients_contract', backref='clients_contract-request_vouchers')
    client_contract_id = Column(Integer, ForeignKey('Clients_contracts.id'), nullable=False)

    services = relationship('Services', backref='services-request_vouchers')
    service_id = Column(Integer, ForeignKey('Services.id'), nullable=False)

    voucher = Column(VARCHAR(length=255), nullable=False)

class Hotels(Base):
    __tablename__ = 'Hotels'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(VARCHAR(length=255), nullable=False)
    count_of_stars = Column(Integer, nullable=False)
    count_of_place = Column(Integer, nullable=False)
    address = Column(VARCHAR(length=255), nullable=False)

    countries = relationship('Countries', backref='countries-hotels')
    country_code = Column(VARCHAR(15), ForeignKey('Countries.code'), nullable=False)

    parking = Column(Boolean, nullable=False)
    transfer = Column(Boolean, nullable=False)

class Hotels_photo(Base):
    __tablename__ = 'Hotels_photo'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    hotels = relationship('Hotels', backref='hotels-hotels_photo')
    hotel_id = Column(Integer, ForeignKey('Hotels.id'), nullable=False)

    photo_url = Column(Text, nullable=False)

class Hotels_inside_tours(Base):
    __tablename__ = 'Hotels_inside_tours'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    hotels = relationship('Hotels', backref='hotels-hotels_inside_tours')
    hotel_id = Column(Integer, ForeignKey('Hotels.id'), nullable=False)

    tours = relationship('Tours', backref='tours-hotels_inside_tours')
    tour_id = Column(Integer, ForeignKey('Tours.id'), nullable=False)

class Services(Base):
    __tablename__ = 'Services'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    partners = relationship('Partners', backref='partners-services')
    partner_id = Column(Integer, ForeignKey('Partners.id'), nullable=False)

    price = Column(DECIMAL(10, 2), nullable=False)
    name = Column(VARCHAR(length=100), nullable=False)

class Services_inside_hotels(Base):
    __tablename__ = 'Services_inside_hotels'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    hotels = relationship('Hotels', backref='hotels-services_inside_hotels')
    hotel_id = Column(Integer, ForeignKey('Hotels.id'), nullable=False)

    services = relationship('Services', backref='services-services_inside_hotels')
    service_id = Column(Integer, ForeignKey('Services.id'), nullable=False)

class Countries(Base):
    __tablename__ = 'Countries'

    code = Column(VARCHAR(length=15), primary_key=True, nullable=False)
    name = Column(VARCHAR(length=255), nullable=False)
    photo_url = Column(Text, nullable=False)

class Hotel_reviews(Base):
    __tablename__ = 'Hotel_reviews'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    hotels = relationship('Hotels', backref='hotels-hotel_reviews')
    hotel_id = Column(Integer, ForeignKey('Hotels.id'), nullable=False)

    clients = relationship('Clients', backref='clients-hotel_reviews')
    client_id = Column(Integer, ForeignKey('Clients.id'), nullable=False)

    content = Column(VARCHAR(length=1000))

class Clients_contracts(Base):
    __tablename__ = 'Clients_contracts'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    clients = relationship('Clients', backref='clients-clients_contracts')
    client_id = Column(Integer, ForeignKey('Clients.id'), nullable=False)

    date_of_contract = Column(DATE, nullable=False)
    name = Column(VARCHAR(length=255), nullable=False)

    tour_requests = relationship('Tour_request', backref='tour_requests-clients_contracts')
    tour_request_id = Column(Integer, ForeignKey('Tour_requests.id'), nullable=False)

metadata = sqlalchemy.MetaData()