import { create } from 'zustand';

type AuthState = {
  accessToken?: string;
  fullName?: string;
  setSession: (accessToken: string, fullName: string) => void;
  clearSession: () => void;
};

export const useAuthStore = create<AuthState>((set) => ({
  setSession: (accessToken, fullName) => set({ accessToken, fullName }),
  clearSession: () => set({ accessToken: undefined, fullName: undefined })
}));
