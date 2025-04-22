import pandas as pd

from behave import given, when, then


@given('product test data is loaded from "{filename}"')
def step_load_test_data(context, filename):
    path = f"features/test_data/{filename}"
    context.df = pd.read_csv(path)
    context.results = []
    print(f"\n Loaded {len(context.df)} test rows from {filename}.csv")

@when("API is called for each input")
def step_call_api_for_inputs(context):
    for _, row in context.df.iterrows():
        input_val = int(row['input'])
        expected = int(row['expected'])

        # Simulating API response (replace this with an actual API call)
        # Example if using real API:
        # response = requests.post("http://api/square", json={"input": input_val})
        # actual = response.json()["result"]
        actual = input_val ** 2

        context.results.append({
            "input": input_val,
            "expected": expected,
            "actual": actual,
            "status": "PASS" if actual == expected else "FAIL"
        })

@then(" Verify that the actual result should match the expected value for all rows")
def step_validate_results(context):
    all_passed = True
    print("\n Test Results:\n----------------")
    for result in context.results:
        print(f"Input: {result['input']} | Expected: {result['expected']} | Actual: {result['actual']} => {result['status']}")
        if result["status"] != "PASS":
            all_passed = False

    # # Optional: Save to Excel
    # df = pd.DataFrame(context.results)
    # df.to_excel("features/test_data/square_test_report.xlsx", index=False)
    # print("\n Report saved to square_test_report.xlsx")
    #
    # assert all_passed, "Some test cases failed!"
