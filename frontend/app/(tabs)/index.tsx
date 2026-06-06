import { ScrollView, StyleSheet } from 'react-native';
import { Text } from 'react-native-paper';
import { FeatureCard } from '@/components/FeatureCard';

export default function HomeScreen() {
  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text variant="headlineLarge">NyayaAI</Text>
      <Text variant="titleMedium">Know Your Rights</Text>
      <FeatureCard title="AI Legal Chat" description="Ask legal-awareness questions with citations and next steps." />
      <FeatureCard title="Evidence Vault" description="Organize images, PDFs, audio, video, tags, and timelines." />
      <FeatureCard title="Case Readiness" description="Find missing documents, risks, and suggested next steps." />
    </ScrollView>
  );
}

const styles = StyleSheet.create({ container: { padding: 20, gap: 8 } });
