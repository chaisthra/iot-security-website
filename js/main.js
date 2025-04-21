/**
 * IoT Security Dashboard JavaScript
 */

document.addEventListener('DOMContentLoaded', function() {
    // Mobile Navigation Toggle
    const navToggle = document.getElementById('nav-toggle');
    const navMenu = document.getElementById('nav-menu');
    
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
        });
    }
    
    // PDF Viewer
    setupPdfViewer();
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Initialize stage tabs if they exist
    const stageTabs = document.getElementById('stage-tabs');
    if (stageTabs) {
        stageTabs.addEventListener('click', function(e) {
            if (e.target.classList.contains('stage-tab')) {
                e.preventDefault();
                
                // Remove active class from all tabs
                document.querySelectorAll('.stage-tab').forEach(tab => {
                    tab.classList.remove('active');
                });
                
                // Add active class to clicked tab
                e.target.classList.add('active');
                
                // Hide all tab content
                document.querySelectorAll('.stage-content').forEach(content => {
                    content.classList.remove('active');
                });
                
                // Show corresponding tab content
                const targetId = e.target.getAttribute('data-target');
                document.getElementById(targetId).classList.add('active');
            }
        });
    }
});

/**
 * Setup PDF Viewer functionality
 */
function setupPdfViewer() {
    const pdfLinks = document.querySelectorAll('.pdf-link');
    const pdfTitle = document.getElementById('pdf-title');
    const pdfDownload = document.getElementById('pdf-download');
    
    pdfLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const pdfPath = this.getAttribute('data-pdf');
            const title = this.textContent.trim();
            
            // Open the PDF in the standalone viewer
            window.open(`pdf_viewer.html?pdf=${encodeURIComponent(pdfPath)}&title=${encodeURIComponent(title)}`, '_blank');
        });
    });
    
    // Load the first PDF by default if available
    if (pdfLinks.length > 0) {
        const firstPdfLink = pdfLinks[0];
        const defaultPdfPath = firstPdfLink.getAttribute('data-pdf');
        const defaultTitle = firstPdfLink.textContent.trim();
        
        // Set the first PDF title and download link
        pdfTitle.textContent = defaultTitle;
        pdfDownload.href = defaultPdfPath;
        pdfDownload.setAttribute('download', defaultTitle + '.pdf');
    }
}

/**
 * Function to navigate between stages
 */
function navigateToStage(stageNumber) {
    // Hide all stage content
    document.querySelectorAll('.stage-content').forEach(content => {
        content.style.display = 'none';
    });
    
    // Show selected stage content
    const selectedStage = document.getElementById(`stage-${stageNumber}-content`);
    if (selectedStage) {
        selectedStage.style.display = 'block';
    }
    
    // Update active class on navigation
    document.querySelectorAll('.stage-nav-item').forEach(item => {
        item.classList.remove('active');
    });
    
    const activeNavItem = document.querySelector(`.stage-nav-item[data-stage="${stageNumber}"]`);
    if (activeNavItem) {
        activeNavItem.classList.add('active');
    }
}

/**
 * Function to toggle stage collapse
 */
function toggleStage(stageId) {
    const stageContent = document.getElementById(`stage-${stageId}-steps`);
    if (stageContent) {
        stageContent.classList.toggle('collapsed');
        
        const toggleIcon = document.querySelector(`#stage-${stageId}-toggle i`);
        if (toggleIcon) {
            if (stageContent.classList.contains('collapsed')) {
                toggleIcon.className = 'fas fa-chevron-down';
            } else {
                toggleIcon.className = 'fas fa-chevron-up';
            }
        }
    }
} 