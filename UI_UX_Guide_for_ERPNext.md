# UI/UX Design Guide: RFID Expo App → ERPNext

A comprehensive design system extracted from the rfid-expo-app for implementation in ERPNext.

---

## Color Palette

### Primary Brand Colors (Indigo/Violet)

| Token | Hex | Usage |
|-------|-----|-------|
| `brand-50` | `#EEF2FF` | Light backgrounds, badges |
| `brand-100` | `#E0E7FF` | Subtle highlights |
| `brand-500` | `#6366F1` | Secondary actions, icons |
| `brand-600` | `#4F46E5` | **Primary brand color**, buttons |
| `brand-700` | `#4338CA` | Hover states |
| `brand-800` | `#3730A3` | Active states |

### Neutral Slate Scale

| Token | Hex | Usage |
|-------|-----|-------|
| `slate-0` | `#FFFFFF` | Cards, surfaces |
| `slate-50` | `#F8FAFC` | **Page background** |
| `slate-100` | `#F1F5F9` | Muted backgrounds |
| `slate-200` | `#E2E8F0` | **Borders** |
| `slate-300` | `#CBD5E1` | Strong borders |
| `slate-400` | `#94A3B8` | Subtle text |
| `slate-500` | `#64748B` | **Muted text** |
| `slate-600` | `#475569` | Secondary text |
| `slate-700` | `#334155` | Emphasized text |
| `slate-800` | `#1E293B` | Strong text |
| `slate-900` | `#0F172A` | **Primary text** |
| `slate-950` | `#020617` | Dark mode backgrounds |

### Semantic Status Colors

| Status | Solid | Background | Foreground | Gradient |
|--------|-------|------------|------------|----------|
| **Pending** | `#F59E0B` | `#FFF7ED` | `#B45309` | `["#F59E0B", "#D97706"]` |
| **Active** | `#3B82F6` | `#EFF6FF` | `#1D4ED8` | `["#3B82F6", "#2563EB"]` |
| **Completed** | `#10B981` | `#ECFDF5` | `#047857` | `["#10B981", "#059669"]` |
| **Cancelled/Danger** | `#EF4444` | `#FEF2F2` | `#B91C1C` | `["#EF4444", "#DC2626"]` |

### Gradient Definitions

```css
/* Brand gradient - for primary buttons, headers */
--gradient-brand: linear-gradient(135deg, #6366F1, #4F46E5, #4338CA);

/* Hero gradient - for splash/hero sections */
--gradient-hero: linear-gradient(135deg, #4F46E5, #7C3AED, #EC4899);

/* Card gradient - subtle depth */
--gradient-card: linear-gradient(135deg, #FFFFFF, #F8FAFC);

/* Status gradients */
--gradient-pending: linear-gradient(135deg, #F59E0B, #D97706);
--gradient-active: linear-gradient(135deg, #3B82F6, #2563EB);
--gradient-success: linear-gradient(135deg, #10B981, #059669);
```

---

## Typography

### Font Stack

```css
font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
```

### Type Scale

| Style | Size | Weight | Letter-spacing | Usage |
|-------|------|--------|----------------|-------|
| Display | 34px | 800 | -0.8px | Hero numbers |
| H1 | 26px | 800 | -0.4px | Page titles |
| H2 | 20px | 700 | -0.2px | Section headers |
| H3 | 17px | 700 | 0 | Card titles |
| Body | 15px | 400 | 0 | Primary text |
| Body Muted | 15px | 400 | 0 | Secondary text |
| Caption | 13px | 400 | 0 | Metadata, labels |
| Overline | 11px | 700 | 0.8px | Labels, eyebrow text |
| Number | 30px | 800 | -0.8px | Stat displays |

---

## Spacing System (4px base)

| Token | Value |
|-------|-------|
| `xs` | 4px |
| `sm` | 8px |
| `md` | 12px |
| `lg` | 16px |
| `xl` | 20px |
| `2xl` | 24px |
| `3xl` | 32px |
| `4xl` | 40px |
| `5xl` | 56px |

---

## Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `xs` | 6px | Small elements |
| `sm` | 10px | Buttons, inputs |
| `md` | 14px | Cards |
| `lg` | 18px | Large cards, modals |
| `xl` | 22px | Hero sections |
| `2xl` | 28px | Featured cards |
| `full` | 999px | Pills, avatars, badges |

---

## Shadows

```css
/* sm - Subtle elevation */
--shadow-sm: 0 1px 2px rgba(15, 23, 42, 0.05);

/* md - Cards, buttons */
--shadow-md: 0 4px 10px rgba(15, 23, 42, 0.08);

/* lg - Elevated cards */
--shadow-lg: 0 10px 20px rgba(15, 23, 42, 0.12);

/* xl - Primary CTAs, floating elements */
--shadow-xl: 0 12px 24px rgba(79, 70, 229, 0.25);
```

---

## Component Patterns

### Cards

```css
.card {
  background: #FFFFFF;
  border-radius: 18px; /* lg */
  border: 1px solid #E2E8F0; /* slate-200 */
  padding: 16px; /* lg */
  box-shadow: 0 4px 10px rgba(15, 23, 42, 0.08);
}
```

### Status Pills

```css
.pill {
  padding: 3px 10px;
  border-radius: 999px; /* full */
  font-size: 12px;
  font-weight: 800;
  /* Colors based on status theme */
}

/* Pending example */
.pill-pending {
  background: #FFF7ED;
  color: #B45309;
}
```

### Primary Buttons (Gradient)

```css
.btn-primary {
  background: linear-gradient(135deg, #6366F1, #4F46E5);
  color: #FFFFFF;
  border-radius: 18px;
  padding: 16px 20px;
  font-weight: 700;
  box-shadow: 0 12px 24px rgba(79, 70, 229, 0.25);
}
```

### Icon Buttons (Glass effect)

```css
.icon-btn {
  width: 42px;
  height: 42px;
  border-radius: 21px;
  background: rgba(255, 255, 255, 0.18);
  border: 1px solid rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(8px);
}
```

### Progress Bars

```css
.progress-track {
  height: 8px;
  background: #F1F5F9;
  border-radius: 4px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  border-radius: 4px;
  background: linear-gradient(90deg, #6366F1, #4338CA);
}
```

---

## ERPNext Implementation Guide

### 1. CSS Custom Properties

Add to your custom app's CSS or `hooks.py`:

```css
:root {
  /* Brand */
  --brand-primary: #4F46E5;
  --brand-primary-dark: #4338CA;
  --brand-light: #EEF2FF;
  
  /* Neutrals */
  --bg-page: #F8FAFC;
  --surface: #FFFFFF;
  --border: #E2E8F0;
  --text-primary: #0F172A;
  --text-muted: #64748B;
  --text-subtle: #94A3B8;
  
  /* Status */
  --status-pending: #F59E0B;
  --status-pending-bg: #FFF7ED;
  --status-active: #3B82F6;
  --status-active-bg: #EFF6FF;
  --status-success: #10B981;
  --status-success-bg: #ECFDF5;
  --status-danger: #EF4444;
  --status-danger-bg: #FEF2F2;
}
```

### 2. Custom Theme JSON (Frappe/ERPNext v14+)

Create in your custom app: `my_app/www/theme.json`

```json
{
  "colors": {
    "primary": "#4F46E5",
    "primary_hover": "#4338CA",
    "background": "#F8FAFC",
    "surface": "#FFFFFF",
    "text": "#0F172A",
    "text_muted": "#64748B",
    "border": "#E2E8F0"
  },
  "border_radius": {
    "sm": "10px",
    "md": "14px",
    "lg": "18px",
    "full": "999px"
  }
}
```

### 3. Form Styles (SCSS)

```scss
// Custom form styling
.form-control {
  border-radius: 10px;
  border: 1px solid #E2E8F0;
  background: #FFFFFF;
  
  &:focus {
    border-color: #6366F1;
    box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
  }
}

.btn-primary {
  background: linear-gradient(135deg, #6366F1, #4F46E5);
  border: none;
  border-radius: 10px;
  font-weight: 600;
  box-shadow: 0 4px 10px rgba(79, 70, 229, 0.25);
  
  &:hover {
    background: linear-gradient(135deg, #4F46E5, #4338CA);
  }
}
```

### 4. Status Badge Component (Jinja2)

```html
{% macro status_badge(status) %}
  {% set themes = {
    'Pending': ('#FFF7ED', '#B45309', '#F59E0B'),
    'In Progress': ('#EFF6FF', '#1D4ED8', '#3B82F6'),
    'Completed': ('#ECFDF5', '#047857', '#10B981'),
    'Cancelled': ('#FEF2F2', '#B91C1C', '#EF4444')
  } %}
  {% set bg, fg, solid = themes.get(status, themes['Pending']) %}
  
  <span class="badge" style="
    background: {{ bg }};
    color: {{ fg }};
    padding: 3px 10px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 700;
    border-left: 3px solid {{ solid }};
  ">
    {{ status }}
  </span>
{% endmacro %}
```

### 5. Dashboard Card Widget (HTML)

```html
<div class="dashboard-card" style="
  background: #FFFFFF;
  border-radius: 18px;
  border: 1px solid #E2E8F0;
  padding: 20px;
  box-shadow: 0 4px 10px rgba(15, 23, 42, 0.08);
">
  <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 16px;">
    <div style="
      width: 44px;
      height: 44px;
      border-radius: 22px;
      background: #EEF2FF;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #4F46E5;
    ">
      <i class="icon">insights</i>
    </div>
    <div>
      <div style="font-size: 11px; font-weight: 700; letter-spacing: 1.2px; color: #64748B;">
        TODAY'S PROGRESS
      </div>
      <div style="font-size: 30px; font-weight: 800; color: #0F172A; letter-spacing: -0.8px;">
        75%
      </div>
    </div>
  </div>
  
  <!-- Progress bar -->
  <div style="height: 10px; background: #F1F5F9; border-radius: 5px; overflow: hidden;">
    <div style="
      height: 100%;
      width: 75%;
      border-radius: 5px;
      background: linear-gradient(90deg, #6366F1, #4F46E5);
    "></div>
  </div>
</div>
```

---

## Key Design Principles

1. **Consistent Rounding** - Use 18px for cards, 10px for buttons, 999px for pills
2. **Soft Shadows** - All elevations use slate-950 (#0F172A) with low opacity
3. **Status Color Coding** - Amber/Blue/Emerald/Red for Pending/Active/Completed/Danger
4. **Gradient Accents** - Primary actions use indigo gradients; status uses solid colors
5. **Whitespace** - Generous 16-20px padding; 12-16px gaps between elements
6. **Typography Hierarchy** - Bold numbers (800 weight), tight letter-spacing on headings
7. **Glass Effects** - White with 18% opacity + subtle border for icon buttons
8. **Left Accent Borders** - 4px colored strip on card left edge for status indication

---

## Source Files

This guide was extracted from the following source files in the rfid-expo-app:

- `/home/rakib/Codes/apps/reder/rfid-expo-app/constants/theme.ts` - Core design tokens
- `/home/rakib/Codes/apps/reder/rfid-expo-app/app/dashboard.tsx` - Dashboard patterns
- `/home/rakib/Codes/apps/reder/rfid-expo-app/app/audits.tsx` - List view patterns
- `/home/rakib/Codes/apps/reder/rfid-expo-app/app/audit/[auditId].tsx` - Detail view patterns
- `/home/rakib/Codes/apps/reder/rfid-expo-app/components/ui/animated-progress.tsx` - Progress component

---

*Generated for ERPNext implementation*
