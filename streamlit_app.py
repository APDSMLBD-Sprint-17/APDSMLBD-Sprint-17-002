import io
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Калькулятор особистого бюджету — квартальний звіт",
    page_icon="📊",
    layout="wide",
)

CATEGORIES = [
    "Їжа",
    "Транспорт",
    "Розваги",
    "Житло / Комунальні",
    "Інше",
]

MONTH_NAMES = ["Місяць 1", "Місяць 2", "Місяць 3"]


def init_session_state() -> None:
    """Ініціалізує стан застосунку."""
    if "monthly_results" not in st.session_state:
        st.session_state.monthly_results = {
            month: None for month in MONTH_NAMES
        }


def calculate_month_budget(income: float, expenses: dict) -> tuple[pd.DataFrame, float, float, str]:
    """
    Розраховує бюджет за місяць.

    Returns:
        df: DataFrame з витратами
        total_expenses: загальна сума витрат
        balance: залишок коштів
        status: статус бюджету
    """
    return df, total_expenses, balance, status


def save_month_result(
    month_name: str,
    income: float,
    df: pd.DataFrame,
    total_expenses: float,
    balance: float,
    status: str,
) -> None:
    """Зберігає результат місяця в session_state."""
    month_df = df.copy()
    month_df["Місяць"] = month_name

    st.session_state.monthly_results[month_name] = {
        "income": income,
        "expenses_df": month_df,
        "total_expenses": total_expenses,
        "balance": balance,
        "status": status,
    }


def render_month_tab(month_name: str) -> None:
    """Відображає вкладку одного місяця."""


def build_quarterly_expenses_df() -> pd.DataFrame:
    """Об'єднує витрати за всі місяці в один DataFrame."""
    return combined_df[["Місяць", "Категорія", "Сума"]]


def build_quarterly_summary_df(combined_df: pd.DataFrame) -> pd.DataFrame:
    """Створює зведення витрат по категоріях."""
    return summary_df


def build_export_csv() -> bytes:
    """Формує CSV-файл квартального звіту."""
    return csv_buffer.getvalue().encode("utf-8-sig")


def render_quarter_report() -> None:
    """Відображає квартальний звіт."""



def main() -> None:
    init_session_state()

    st.title("💰 Калькулятор особистого бюджету — рівень 2")
    st.write(
        "Додаток дозволяє вести бюджет за 3 місяці та формувати зведений квартальний звіт."
    )

    section = st.sidebar.radio(
        "Навігація",
        ["Місячні дані", "Квартальний звіт"],
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("### Стан заповнення")
    for month_name in MONTH_NAMES:
        if st.session_state.monthly_results.get(month_name) is not None:
            st.sidebar.success(f"{month_name}: готово")
        else:
            st.sidebar.info(f"{month_name}: немає розрахунку")

    if section == "Місячні дані":
        st.header("📅 Дані по місяцях")
        tabs = st.tabs(MONTH_NAMES)

        for tab, month_name in zip(tabs, MONTH_NAMES):
            with tab:
                render_month_tab(month_name)

    elif section == "Квартальний звіт":
        render_quarter_report()


if __name__ == "__main__":
    main()
