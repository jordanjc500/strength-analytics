# Strength Analytics

A personal Python project designed to measure and analyze strength across workouts and exercises, with the long-term goal of providing insights into training performance and visualizing user-provided data.

## Current Features

- Graphical user interface built using Tkinter
- Estimated one-rep max (1RM) calculation using the Epley formula
- User-provided weight and repetition inputs
- Dynamic display of calculated results
- Conditional warning for unusually high weight inputs
- Weight rounding and barbell plate-loading calculations in the calculation module (not yet integrated into the GUI)

## Running the Application

Requires Python 3 with Tkinter available.

1. Clone the repository:

   ```bash
   git clone https://github.com/jordanjc500/strength-analytics.git
   ```

2. Navigate into the project directory:

   ```bash
   cd strength-analytics
   ```

3. Run the application:

   ```bash
   python interface.py
   ```

No additional third-party packages are required for the current version.

## Project Structure

- `interface.py` — Tkinter graphical interface and user interactions
- `workoutcalcs.py` — Strength estimation and plate-loading calculations

## Planned Features

- Basic input validation
- Integrate the plate calculator into the graphical interface
- Support pounds and kilograms with configurable barbell weights
- Customizable plate inventories
- Additional strength estimation methods
- Workout history and performance analysis
- Data visualization and progress tracking

## Project Status

Early development. The current application provides an interactive 1RM estimator, with additional calculations and analytical features under development.