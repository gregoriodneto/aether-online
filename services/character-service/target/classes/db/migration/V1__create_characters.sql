CREATE TABLE characters (
    id UUID PRIMARY KEY,
    server_id UUID NOT NULL,
    name VARCHAR(50) NOT NULL,
    character_class VARCHAR(30) NOT NULL,
    level INTEGER NOT NULL DEFAULT 1,
    version BIGINT NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    CONSTRAINT chk_character_level
        CHECK (level >= 1),

    CONSTRAINT chk_character_name
        CHECK (LENGTH(TRIM(name)) BETWEEN 3 AND 50)
);

CREATE UNIQUE INDEX uk_character_server_name
ON characters (server_id, LOWER(name));