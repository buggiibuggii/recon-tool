import { PropsWithChildren } from 'react';
import { StyleSheet } from 'react-native';
import { Card, Text } from 'react-native-paper';

type Props = PropsWithChildren<{ title: string; description: string }>;

export function FeatureCard({ title, description, children }: Props) {
  return (
    <Card style={styles.card}>
      <Card.Content>
        <Text variant="titleMedium">{title}</Text>
        <Text variant="bodyMedium">{description}</Text>
        {children}
      </Card.Content>
    </Card>
  );
}

const styles = StyleSheet.create({ card: { marginBottom: 12 } });
