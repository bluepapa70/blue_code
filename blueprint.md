# Blueprint: Bluepapa AI Lotto Number Generator

## Overview
A web-based Lotto number generator that provides number recommendations based on historical frequency data (2002.12 ~ 2026.05). It uses modern web technologies including CSS variables and vanilla JavaScript to provide a responsive and interactive user experience.

## Project Outline
- **Entry Point**: `index.html`
- **Styling**: Modern CSS with flexbox, grid, and custom properties.
- **Features**:
  - Frequency-based recommendation.
  - Pure random recommendation.
  - Top N fixed number recommendation.
  - Historical frequency statistics panel with sorting.
  - Responsive design for mobile and desktop.

## Current Planned Changes: Dark/Light Mode Implementation
### Purpose
Allow users to switch between dark and light themes for better accessibility and user preference.

### Implementation Steps
1. **Refactor Codebase**:
   - Extract internal CSS from `index.html` to `style.css`.
   - Extract internal JavaScript from `index.html` to `main.js`.
   - Link `style.css` and `main.js` in `index.html`.
2. **Define Theme Variables**:
   - Update `style.css` to use CSS variables for all theme-related colors.
   - Define a default light theme and a `.dark-mode` override.
3. **Add Toggle UI**:
   - Add a theme toggle button (icon-based) in the header of `index.html`.
4. **Implement Toggle Logic**:
   - Add a `toggleTheme()` function in `main.js`.
   - Use `localStorage` to persist the user's theme preference.
   - Apply the correct theme on page load based on the stored preference or system settings.
5. **Git Push**:
   - Commit and push the changes to the remote repository.
