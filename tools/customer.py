import os
from pathlib import Path
from typing import Any

import psycopg
from dotenv import load_dotenv
from langchain.tools import tool
from psycopg.rows import dict_row


@tool
def user_brief(customer: str) -> list[dict[str, Any]]:
    """Look up a user's information and recorded profile before answering or drafting.

    Args:
        customer: username, such as ashayas or p2arthur

    Returns:
        Matching record with id, username, skillset, experience and techstack; an empty list if unknown
    """
    customer = customer.strip()
    if not customer:
        return []

    load_dotenv(Path(__file__).resolve().parents[1] / ".env")
    with psycopg.Connection[dict[str, Any]].connect(
        os.environ["DATABASE_URL"], row_factory=dict_row, connect_timeout=5
    ) as conn:
        return conn.execute(
            """
            SELECT
                u.id,
                u.username,
                p.result #> '{judgment,specialties}' AS skillset,
                p.result #> '{judgment,experience}' AS experience,
                p.result #> '{judgment,stack}' AS techstack
            FROM "User" u
            LEFT JOIN "ProfileJudgment" p ON p."userId" = u.id
            WHERE lower(u.username) = lower(%s)
            """,
            (customer,),
        ).fetchall()
