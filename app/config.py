from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    line_channel_secret: str
    line_channel_access_token: str

    odoo_url: str
    odoo_db: str
    odoo_username: str
    odoo_password: str
    odoo_helpdesk_team_id: int = 1

    anthropic_api_key: str
    google_api_key: str

    class Config:
        env_file = ".env"


settings = Settings()
