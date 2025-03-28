# Backend README

# Food Surplus Insights System - Backend

This is the backend part of the Food Surplus Insights project, built using Python and Flask.

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone 
   cd food-surplus-insights/backend
   ```

2. **Create a virtual environment (optional but recommended):**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   python run.py
   ```

## Usage

Once the application is running, the API is at `http://localhost:5002. 

## API Endpoints

- \*\*GET /requests\*\*: Returns the total number of requests by area.
- \*\*GET /weights\*\*: Returns the total weight by area.
- \*\*GET /heatmap\*\*: Generates a heatmap of weights by area within a specified date range.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes. 

## License

This project is licensed under the MIT License.