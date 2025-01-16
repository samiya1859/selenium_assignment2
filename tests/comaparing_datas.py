def compare_field(field_name, tile_value, map_value, detail_value, comparison_result):
    """
    Compares a specific field from tile, map, and detail data.
    
    Args:
    - field_name (str): The name of the field being compared.
    - tile_value, map_value, detail_value: Values to compare from tile, map, and detail.
    - comparison_result (dict): The result dictionary to update.
    """
    if tile_value != map_value:
        comparison_result["passed"] = False
        
    if map_value != detail_value:
        comparison_result["passed"] = False
    

def compare_data(tile_data, map_data, detail_data):
    """
    Compares the data from the tile, map, and detail page.

    Args:
    - tile_data, map_data, detail_data (dict): Data extracted from each source

    Returns:
    - comparison_result (dict): Contains test case result, pass/fail, and comments.
    """
    comparison_result = {
        "test_case": "Compare tile, map, and detail data",
        "passed": True,
        "comments": []
    }

    # Use the helper function for each field
    compare_field("Title", tile_data.get('title'), map_data.get('title'), detail_data.get('title'), comparison_result)
    compare_field("Price", tile_data.get('price'), map_data.get('price'), detail_data.get('price'), comparison_result)
    compare_field("Type", tile_data.get('type'), map_data.get('type'), detail_data.get('type'), comparison_result)
    compare_field("Rating", tile_data.get('rating'), map_data.get('rating'), detail_data.get('rating'), comparison_result)
    compare_field("Reviews", tile_data.get('reviews'), map_data.get('reviews'), detail_data.get('reviews'), comparison_result)

    # Add final data comparison for reference
    comparison_result["comments"].append(
        f"Data comparison: tile_info={tile_data}, map_info={map_data}, detail_info={detail_data}"
    )

    return comparison_result
