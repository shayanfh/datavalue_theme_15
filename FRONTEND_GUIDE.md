# راهنمای تم و فرانت‌اند اپلیکیشن Maraseel Audit

## مقدمه
این راهنما برای پیاده‌سازی تم و طراحی فرانت‌اند اپلیکیشن Maraseel Audit در وب‌سایت شما طراحی شده است. اپلیکیشن از React Native با Expo ساخته شده و دارای سیستم تم‌بندی جامع و کامپوننت‌های طراحی شده است.

## ساختار کلی تم

### 1. رنگ‌ها (Palette)
```typescript
// رنگ‌های اصلی برند
brand: {
  50: "#EEF2FF",   // بسیار روشن
  100: "#E0E7FF",  // روشن
  200: "#C7D2FE",  // نیمه‌روشن
  500: "#6366F1",  // اصلی
  600: "#4F46E5",  // تیره‌تر
  700: "#4338CA",  // تیره
  800: "#3730A3",  // بسیار تیره
}

// رنگ‌های خاکستری
slate: {
  0: "#FFFFFF",    // سفید
  50: "#F8FAFC",   // پس‌زمینه اصلی
  100: "#F1F5F9",  // پس‌زمینه سطحی
  200: "#E2E8F0",  // مرزها
  300: "#CBD5E1",  // مرزهای قوی
  400: "#94A3B8",  // متن نیمه‌روشن
  500: "#64748B",  // متن ملایم
  600: "#475569",  // متن متوسط
  700: "#334155",  // متن تیره
  800: "#1E293B",  // متن بسیار تیره
  900: "#0F172A",  // متن اصلی
}

// رنگ‌های وضعیت
warning: { 500: "#F59E0B", 600: "#D97706", 700: "#B45309" }
success: { 500: "#10B981", 600: "#059669", 700: "#047857" }
danger: { 500: "#EF4444", 600: "#DC2626", 700: "#B91C1C" }
info: { 500: "#3B82F6", 600: "#2563EB", 700: "#1D4ED8" }
```

### 2. گرادیانت‌ها (Gradients)
```typescript
brand: ["#6366F1", "#4F46E5", "#4338CA"]
brandSoft: ["#EEF2FF", "#E0E7FF"]
hero: ["#4F46E5", "#7C3AED", "#EC4899"]
card: ["#FFFFFF", "#F8FAFC"]
```

### 3. فاصله‌گذاری (Spacing)
```typescript
xs: 4, sm: 8, md: 12, lg: 16, xl: 20, xxl: 24, "3xl": 32, "4xl": 40, "5xl": 56
```

### 4. شعاع‌های گرد (Radius)
```typescript
xs: 6, sm: 10, md: 14, lg: 18, xl: 22, "2xl": 28, full: 999
```

### 5. سایه‌ها (Shadows)
```typescript
sm: { shadowColor: "#0F172A", shadowOffset: {width: 0, height: 1}, shadowOpacity: 0.05, shadowRadius: 2 }
md: { shadowColor: "#0F172A", shadowOffset: {width: 0, height: 4}, shadowOpacity: 0.08, shadowRadius: 10 }
lg: { shadowColor: "#0F172A", shadowOffset: {width: 0, height: 10}, shadowOpacity: 0.12, shadowRadius: 20 }
xl: { shadowColor: "#4F46E5", shadowOffset: {width: 0, height: 12}, shadowOpacity: 0.25, shadowRadius: 24 }
```

### 6. تایپوگرافی (Typography)
```typescript
display: { fontSize: 34, fontWeight: "800", letterSpacing: -0.8 }
h1: { fontSize: 26, fontWeight: "800", letterSpacing: -0.4 }
h2: { fontSize: 20, fontWeight: "700", letterSpacing: -0.2 }
h3: { fontSize: 17, fontWeight: "700" }
body: { fontSize: 15 }
bodyMuted: { fontSize: 15, color: textMuted }
caption: { fontSize: 13, color: textMuted }
overline: { fontSize: 11, fontWeight: "700", letterSpacing: 0.8, textTransform: "uppercase" }
number: { fontSize: 30, fontWeight: "800", letterSpacing: -0.8 }
```

## کامپوننت‌های پایه

### 1. ThemedText
کامپوننت متنی که از تم پیروی می‌کند:
```jsx
<ThemedText type="h1">عنوان اصلی</ThemedText>
<ThemedText type="body">متن معمولی</ThemedText>
<ThemedText type="caption" style={{color: Colors.primary}}>متن توضیح</ThemedText>
```

### 2. ThemedView
کامپوننت view که رنگ پس‌زمینه تم‌دار دارد:
```jsx
<ThemedView style={{padding: Spacing.lg}}>
  <Text>محتوا</Text>
</ThemedView>
```

### 3. IconSymbol
آیکون‌های سازگار با پلتفرم:
```jsx
<IconSymbol name="house.fill" size={24} color={Colors.primary} />
<IconSymbol name="chevron.right" size={20} color={Colors.textMuted} />
```

## کامپوننت‌های UI

### 1. کارت آمار (StatCard)
کارت‌های آمار با آیکون و گرادیانت وضعیت:
```jsx
<View style={styles.statsContainer}>
  <StatCard
    label="Pending"
    count={5}
    icon="pending-actions"
    statusKey="pending"
    onPress={handlePress}
  />
</View>
```

### 2. کارت ممیزی (AuditCard)
کارت نمایش ممیزی با نوار پیشرفت:
```jsx
<TouchableOpacity style={styles.auditCard}>
  <View style={[styles.auditAccent, {backgroundColor: theme.solid}]} />
  <View style={styles.auditCardRow}>
    {/* محتوا */}
  </View>
  <AnimatedProgress value={75} gradient={theme.gradient} height={6} />
</TouchableOpacity>
```

### 3. نوار پیشرفت متحرک (AnimatedProgress)
```jsx
<AnimatedProgress
  value={75}
  gradient={Gradients.brand}
  height={10}
/>
```

### 4. عدد متحرک (AnimatedNumber)
```jsx
<AnimatedNumber value={count} style={styles.largeNumber} />
```

### 5. اسکلتون لودینگ (Skeleton)
```jsx
<Skeleton width="60%" height={16} />
<Skeleton width="100%" height={12} style={{marginTop: Spacing.sm}} />
```

## الگوهای طراحی

### 1. هدر اصلی
```jsx
<LinearGradient colors={Gradients.hero} style={styles.headerBg}>
  <View style={styles.header}>
    <TouchableOpacity style={styles.iconBtn}>
      <IconSymbol name="line.3.horizontal" size={22} color="#fff" />
    </TouchableOpacity>
    <View style={styles.headerCenter}>
      <Text style={styles.headerEyebrow}>MARASEEL</Text>
      <Text style={styles.headerTitle}>Asset Audit</Text>
    </View>
    <TouchableOpacity style={styles.iconBtn}>
      <IconSymbol name="arrow.clockwise" size={22} color="#fff" />
    </TouchableOpacity>
  </View>
</LinearGradient>
```

### 2. کارت خلاصه
```jsx
<View style={styles.summaryCard}>
  <LinearGradient colors={Gradients.card} style={StyleSheet.absoluteFill} />
  <View style={styles.summaryContent}>
    <Text style={styles.summaryEyebrow}>TODAY'S PROGRESS</Text>
    <View style={styles.numberRow}>
      <AnimatedNumber value={75} style={styles.largePercent} />
      <Text style={styles.percentSuffix}>%</Text>
    </View>
  </View>
</View>
```

### 3. دکمه اقدام سریع
```jsx
<TouchableOpacity activeOpacity={0.9}>
  <LinearGradient colors={Gradients.brand} style={styles.actionButton}>
    <View style={styles.actionLeft}>
      <View style={styles.actionIcon}>
        <IconSymbol name="checkmark.circle.fill" size={22} color="#fff" />
      </View>
      <View>
        <Text style={styles.actionTitle}>All Audits</Text>
        <Text style={styles.actionSubtitle}>View complete list</Text>
      </View>
    </View>
    <IconSymbol name="chevron.right" size={22} color="#fff" />
  </LinearGradient>
</TouchableOpacity>
```

## سیستم وضعیت‌ها

اپلیکیشن از سیستم وضعیت‌های رنگی استفاده می‌کند:

```typescript
const StatusTheme = {
  pending: {
    solid: Palette.warning[500],
    bg: Palette.warning[50],
    fg: Palette.warning[700],
    gradient: [Palette.warning[500], Palette.warning[600]]
  },
  active: {
    solid: Palette.info[500],
    bg: Palette.info[50],
    fg: Palette.info[700],
    gradient: [Palette.info[500], Palette.info[600]]
  },
  completed: {
    solid: Palette.success[500],
    bg: Palette.success[50],
    fg: Palette.success[700],
    gradient: [Palette.success[500], Palette.success[600]]
  }
}
```

## انیمیشن‌ها

### 1. ورود عناصر (FadeIn)
```jsx
<Animated.View entering={FadeInDown.duration(500).springify()}>
  {/* محتوا */}
</Animated.View>
```

### 2. انیمیشن‌های زنجیره‌ای
```jsx
<Animated.View entering={FadeInDown.delay(120).duration(500).springify()}>
  {/* محتوا */}
</Animated.View>
```

## نکات پیاده‌سازی

### 1. ساختار فایل‌ها
```
constants/
  theme.ts          # تعریف تم اصلی
components/
  themed-text.tsx   # کامپوننت متن تم‌دار
  themed-view.tsx   # کامپوننت view تم‌دار
  ui/               # کامپوننت‌های UI قابل استفاده مجدد
    skeleton.tsx
    animated-progress.tsx
    ...
```

### 2. وابستگی‌های کلیدی
- `expo-linear-gradient` برای گرادیانت‌ها
- `@expo/vector-icons/MaterialIcons` برای آیکون‌ها
- `react-native-reanimated` برای انیمیشن‌ها
- `react-native-safe-area-context` برای safe area

### 3. نکات responsive
- استفاده از `Spacing` برای فاصله‌گذاری ثابت
- استفاده از `Radius` برای گرد کردن گوشه‌ها
- استفاده از `Shadows` برای عمق‌بخشی

### 4. تم تیره/روشن
اپلیکیشن از سیستم خودکار تم تیره/روشن استفاده می‌کند که می‌توانید آن را گسترش دهید.

## مثال پیاده‌سازی کامل

```jsx
import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { Colors, Spacing, Radius, Gradients, Typography, Shadows } from './constants/theme';
import { ThemedText } from './components/themed-text';
import { IconSymbol } from './components/ui/icon-symbol';

export default function Dashboard() {
  return (
    <View style={styles.container}>
      {/* هدر گرادیانت */}
      <LinearGradient colors={Gradients.hero} style={styles.heroBg}>
        <View style={styles.header}>
          <ThemedText style={styles.headerTitle}>Maraseel Audit</ThemedText>
        </View>
      </LinearGradient>

      {/* کارت آمار */}
      <View style={styles.statsContainer}>
        <TouchableOpacity style={styles.statCard}>
          <LinearGradient colors={Gradients.card} style={StyleSheet.absoluteFill} />
          <View style={styles.statIcon}>
            <IconSymbol name="pending-actions" size={24} color="#F59E0B" />
          </View>
          <ThemedText style={styles.statCount}>5</ThemedText>
          <ThemedText style={styles.statLabel}>Pending</ThemedText>
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: Colors.bg },
  heroBg: { height: 200 },
  header: { padding: Spacing.lg },
  headerTitle: { ...Typography.h1, color: '#fff' },
  statsContainer: { padding: Spacing.lg },
  statCard: {
    backgroundColor: '#fff',
    borderRadius: Radius.lg,
    padding: Spacing.lg,
    alignItems: 'center',
    ...Shadows.md
  },
  statIcon: {
    width: 48,
    height: 48,
    borderRadius: 24,
    backgroundColor: '#FEF3C7',
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: Spacing.sm
  },
  statCount: { ...Typography.number, color: Colors.text },
  statLabel: { ...Typography.overline, color: Colors.textMuted }
});
```

این راهنما شامل تمام عناصر طراحی اپلیکیشن Maraseel Audit است. با پیروی از این الگوها می‌توانید طراحی یکسانی در وب‌سایت خود پیاده‌سازی کنید.