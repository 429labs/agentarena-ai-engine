from sqlalchemy import Column, Integer, BigInteger, String, Boolean, Numeric, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Round(Base):
    __tablename__ = 'rounds'

    id = Column(BigInteger, primary_key=True)
    round_name = Column(String(100), nullable=False)
    round_description = Column(String, nullable=False)
    start_date = Column(TIMESTAMP(timezone=True), server_default=func.now())
    end_date = Column(TIMESTAMP(timezone=True), server_default=func.now())
    prize_pool = Column(Numeric(20, 6), nullable=True)
    is_locked = Column(Boolean, nullable=False, default=False)
    is_processed = Column(Boolean, nullable=False, default=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())


class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True)
    wallet_address = Column(String(100), nullable=False)
    username = Column(String(50), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())


class Boss(Base):
    __tablename__ = 'bosses'

    id = Column(BigInteger, primary_key=True)
    round_id = Column(BigInteger, ForeignKey('rounds.id'), nullable=False)
    boss_name = Column(String(100), nullable=False)
    hp = Column(Integer, nullable=False)
    atk = Column(Integer, nullable=False)
    defense = Column(Integer, nullable=False)
    stamina = Column(Integer, nullable=False)
    image_url = Column(String(255), nullable=True)
    strategy_prompt = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())


class Participant(Base):
    __tablename__ = 'participants'

    id = Column(BigInteger, primary_key=True)
    round_id = Column(BigInteger, ForeignKey('rounds.id'), nullable=False)
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    has_paid = Column(Boolean, nullable=False, default=False)
    hp = Column(Integer, nullable=False)
    atk = Column(Integer, nullable=False)
    defense = Column(Integer, nullable=False)
    stamina = Column(Integer, nullable=False)
    strategy_prompt = Column(Text, nullable=True)
    joined_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())


class Fight(Base):
    __tablename__ = 'fights'

    id = Column(BigInteger, primary_key=True)
    round_id = Column(BigInteger, ForeignKey('rounds.id'), nullable=False)
    participant_id = Column(BigInteger, ForeignKey('participants.id'), nullable=False)
    boss_id = Column(BigInteger, ForeignKey('bosses.id'), nullable=False)
    did_win = Column(Boolean, nullable=False)
    final_hp_player = Column(Integer, nullable=False)
    final_hp_boss = Column(Integer, nullable=False)
    fight_log = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())


class Payout(Base):
    __tablename__ = 'payouts'

    id = Column(BigInteger, primary_key=True)
    round_id = Column(BigInteger, ForeignKey('rounds.id'), nullable=False)
    participant_id = Column(BigInteger, ForeignKey('participants.id'), nullable=False)
    payout_amount = Column(Numeric(20, 6), nullable=False)
    transaction_id = Column(BigInteger, nullable=True)
    distributed_at = Column(TIMESTAMP(timezone=True))
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())
