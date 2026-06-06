import { Tabs } from 'expo-router';

export default function TabsLayout() {
  return (
    <Tabs>
      <Tabs.Screen name="index" options={{ title: 'Home' }} />
      <Tabs.Screen name="chat" options={{ title: 'Chat' }} />
      <Tabs.Screen name="constitution" options={{ title: 'Constitution' }} />
      <Tabs.Screen name="guides" options={{ title: 'Guides' }} />
      <Tabs.Screen name="evidence" options={{ title: 'Evidence' }} />
      <Tabs.Screen name="settings" options={{ title: 'Settings' }} />
    </Tabs>
  );
}
