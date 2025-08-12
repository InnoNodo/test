CREATE TABLE IF NOT EXISTS users (
  id BIGSERIAL PRIMARY KEY,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS balances (
  user_id BIGINT PRIMARY KEY REFERENCES users(id),
  current NUMERIC(20,4) NOT NULL DEFAULT 0,
  maximum NUMERIC(20,4) NOT NULL DEFAULT 0,
  locked NUMERIC(20,4) NOT NULL DEFAULT 0,
  updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS transactions (
  id UUID PRIMARY KEY,
  user_id BIGINT NOT NULL REFERENCES users(id),
  amount NUMERIC(20,4) NOT NULL,
  state TEXT NOT NULL,
  owner_service TEXT NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now(),
  expires_at timestamptz NULL,
  metadata JSONB NULL
);

CREATE INDEX IF NOT EXISTS idx_tx_user_state ON transactions (user_id, state);
CREATE INDEX IF NOT EXISTS idx_tx_expires ON transactions (expires_at);