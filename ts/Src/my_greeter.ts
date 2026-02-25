class My_greeter {
    private greeting(): string {
        let hour = new Date().getHours();
        if (hour >= 6 && hour < 12) {
            return "Good morning";
        } else if (hour >= 12 && hour < 18) {
            return "Good afternoon";
        } else if (hour >= 18 && hour <= 23) {
            return "Good evening";
        }
    }
}
