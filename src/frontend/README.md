# Frontend – Patent Application Generator (HTML)

This directory will contain the HTML5 frontend templates and static assets served by CakePHP.

## Structure (Sprint 8+)

```
frontend/
├── templates/
│   ├── layout/
│   │   └── default.php          # Base layout
│   ├── Patents/
│   │   ├── index.php            # Patent list page
│   │   ├── add.php              # Patent submission form
│   │   └── view.php             # Draft review and edit page
│   └── Users/
│       └── login.php            # Login page
└── webroot/
    ├── css/
    │   ├── base.css             # Base styles
    │   └── components.css       # Component styles (BEM)
    └── js/
        ├── job-status.js        # Real-time job status polling
        └── draft-editor.js      # Draft inline editing
```

## Design Principles

- **HTML5 semantic elements** throughout.
- **CSS BEM naming convention** for all classes.
- **No inline styles or scripts**; all in external files.
- **WCAG 2.1 Level AA** accessibility compliance.
- **Progressive disclosure**: advanced options hidden behind expandable sections.

## Related Documents

- [Conceptual Design](../../docs/design/conceptual_design.md)
- [System Architecture](../../docs/architecture/system_architecture.md)
- [Implementation Plan – Sprint 8](../../docs/plans/implementation_plan.md)
