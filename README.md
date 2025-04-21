# IoT Security Threat Detection Dashboard

This interactive dashboard provides access to all PDF reports and visualizations from the "IoT Security Threat Detection for SMEs" case study. It organizes the research documents by stages and provides a responsive PDF viewer for convenient access to the research materials.

## Features

- Interactive dashboard with all research PDFs organized by stages
- Responsive standalone PDF viewer with download capabilities
- Mobile-friendly design that works across all device types
- Comprehensive overview of the research methodology
- Simple Python-based server for local viewing

## Getting Started

### Prerequisites

- Python 3.x
- Web browser (Chrome, Firefox, Safari, or Edge recommended)

### Running the Website Locally

1. Navigate to the website directory:
   ```
   cd website
   ```

2. Run the Python server script:
   ```
   python server.py
   ```

3. The server will start and automatically open your default web browser to the dashboard.
   If it doesn't open automatically, visit: http://localhost:8000

4. To stop the server, press `Ctrl+C` in the terminal.

5. Verify the website configuration:
   ```
   python check_website.py
   ```

## Dashboard Structure

The dashboard is organized into the following sections:

1. **Home** - Introduction to the case study
2. **Methodology** - Overview of the research approach
3. **Dashboard** - Main section with access to all PDF reports organized by research stages
4. **About** - Information about research objectives and dataset

### Research Stages

The case study is organized into seven stages:

1. **Preliminary Assessment** - Dataset familiarization, attack pattern analysis, SME context definition, critical metrics identification
2. **Data Preparation** - Quality assessment, feature engineering
3. **Exploratory Analysis** - Pattern analysis, correlation analysis, anomaly identification
4. **Model Development** - Base model development, SME-optimized learning
5. **Validation & Refinement** - Performance metrics, domain expert validation
6. **Reporting & Visualization** - Results documentation and visualization
7. **Recommendations** - Implementation framework, future enhancement areas

## PDF Viewer

The dashboard includes a responsive standalone PDF viewer that provides:

- Mobile-friendly viewing experience
- Direct access to any PDF in the research collection
- Download option for offline viewing
- Easy navigation back to the main dashboard

## Recent Updates

- **Responsive PDF Viewer**: Added a standalone PDF viewer that works on all devices
- **Updated PDF Links**: All PDF links now use the new viewer for better mobile compatibility
- **Researcher Information**: Added detailed researcher credits in the footer
- **Website Checker**: Added a script to verify website configuration

## Troubleshooting

- **PDF Viewer Issues**: If PDFs don't load in the viewer, try the download button to view them directly.
- **Port Already in Use**: The server will automatically try the next available port if 8000 is already in use.
- **Missing PDFs**: Make sure all PDFs are in the correct `output` directory. The relative path structure is important.
- **Font Issues**: If you're generating new PDFs, ensure the DejaVu fonts are installed in the `fonts` directory.

## Credits

This dashboard was created for the "IoT Security Threat Detection for SMEs" case study, a comprehensive research project analyzing the CIC-IoT dataset to develop machine learning approaches for security threat detection in SME environments.

**Researchers**:
- Chaithra N, Janhvi Jha (Dept of Computer Science and Engineering, AI & ML, Jain University, Bangalore, India)
- Dr Anu Sayal (Senior Lecturer, Taylor's Business School, Taylor's University, Malaysia) 