from datetime import datetime
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = PROJECT_ROOT / ".env"


def load_env(path: Path) -> dict[str, str]:
    config = {}

    for line in path.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue

        key, value = line.split("=", 1)
        config[key] = value

    return config
    # this is a cool function
    # second comment to that 33


def main() -> None:
    config = load_env(ENV_PATH)

    company_name = config["COMPANY_NAME"]
    input_path = PROJECT_ROOT / config["INPUT_DATA_PATH"]
    output_folder = PROJECT_ROOT / config["OUTPUT_FOLDER"]
    output_prefix = config["OUTPUT_PREFIX"]

    data = pd.read_csv(input_path)
    data["profit_usd"] = data["revenue_usd"] - data["cost_usd"]

    summary_by_channel = (
        data.groupby("channel", as_index=False)
        .agg(
            campaigns=("campaign_id", "count"),
            total_cost_usd=("cost_usd", "sum"),
            total_revenue_usd=("revenue_usd", "sum"),
            total_profit_usd=("profit_usd", "sum"),
        )
        .sort_values("total_profit_usd", ascending=False)
    )

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = output_folder / f"{output_prefix}_{timestamp}.xlsx"
    output_folder.mkdir(parents=True, exist_ok=True)

    with pd.ExcelWriter(output_path) as writer:
        data.to_excel(writer, sheet_name="campaigns", index=False)
        summary_by_channel.to_excel(writer, sheet_name="summary", index=False)

    print(f"Analysis complete for {company_name}")
    print(f"Excel file created: {output_path}")


if __name__ == "__main__":
    main()
