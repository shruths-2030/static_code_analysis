"""
Inventory System Module

This module handles inventory operations such as adding,
removing, loading, saving, and reporting stock information.
"""

import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s"
)

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Add specified quantity of item to the inventory.

    Args:
        item (str): Item name
        qty (int): Quantity to add
        logs (list): Optional list to capture log messages
    """
    if logs is None:
        logs = []

    if not isinstance(item, str):
        logging.error(
            "Invalid item type: expected str, got %s", type(item).__name__
        )
        return
    if not isinstance(qty, int):
        logging.error(
            "Invalid quantity type for item '%s': expected int, got %s",
            item,
            type(qty).__name__,
        )
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(
        "%s: Added %d of %s"
        % (str(datetime.now()), qty, item)
    )


def remove_item(item, qty):
    """
    Remove specified quantity of item from the inventory.

    Args:
        item (str): Item name
        qty (int): Quantity to remove
    """
    if not isinstance(item, str):
        logging.error("Invalid item type: expected str, got %s", type(item).__name__)
        return
    if not isinstance(qty, int):
        logging.error(
            "Invalid quantity type for item '%s': expected int, got %s",
            item,
            type(qty).__name__,
        )
        return

    try:
        if item not in stock_data:
            logging.warning("Item '%s' not found in stock_data.", item)
            return

        stock_data[item] -= qty

        if stock_data[item] <= 0:
            del stock_data[item]

    except KeyError:
        logging.warning(
            "Attempted to remove an item that does not exist in stock_data."
        )


def get_qty(item):
    """
    Get the quantity of the given item in stock.

    Args:
        item (str): Item name

    Returns:
        int: Quantity of item or 0 if not found
    """
    if not isinstance(item, str):
        logging.error("Invalid item type: expected str, got %s", type(item).__name__)
        return 0
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """
    Load inventory data from a JSON file.

    Args:
        file (str): Filename to load from
    """
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        logging.warning("File %s not found. Starting with empty stock.", file)
    except json.JSONDecodeError as e:
        logging.error("Error decoding JSON from file %s: %s", file, e)


def save_data(file="inventory.json"):
    """
    Save inventory data to a JSON file.

    Args:
        file (str): Filename to save to
    """
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
    except Exception as e:
        logging.error("Error saving data to file %s: %s", file, e)


def print_data():
    """
    Print a report of all items and their quantities.
    """
    print("Items Report")
    for i in stock_data:
        print("%s -> %d" % (i, stock_data[i]))


def check_low_items(threshold=5):
    """
    Return list of items with quantity less than threshold.

    Args:
        threshold (int): Threshold quantity, default 5

    Returns:
        list: List of low stock item names
    """
    return [i for i in stock_data if stock_data[i] < threshold]


def main():
    """
    Main program flow for inventory management.
    """
    logs = []
    add_item("apple", 10, logs)
    add_item("banana", -2, logs)
    add_item("123", 10, logs)  # Corrected to string type item
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()

    # Removed unsafe eval usage and replaced with safe logging message
    logging.info("Eval usage replaced with safe logging.")


if __name__ == "__main__":
    main()
