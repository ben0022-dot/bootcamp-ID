
// Base interface with readonly property
interface User {
    readonly id: number;      // Cannot be changed after creation
    name: string;
    email: string;
}

// Extended interface with optional property (marked with ?)
interface PremiumUser extends User {
    membershipLevel?: string;  // Optional - may or may not be provided
    readonly joinedDate: Date; // Additional readonly property
}

// Function that accepts PremiumUser
function printUserDetails(user: PremiumUser): void {
    console.log("===== User Details =====");
    console.log(`ID: ${user.id}`);
    console.log(`Name: ${user.name}`);
    console.log(`Email: ${user.email}`);
    
    // Check if optional property exists
    if (user.membershipLevel) {
        console.log(`Membership Level: ${user.membershipLevel}`);
    } else {
        console.log("Membership Level: Standard (Free)");
    }
    
    console.log(`Joined: ${user.joinedDate.toDateString()}`);
    console.log("=======================");
}

// Usage examples
const regularPremium: PremiumUser = {
    id: 1,
    name: "John Doe",
    email: "john@example.com",
    membershipLevel: "Gold",
    joinedDate: new Date("2023-01-15")
};

const freeUser: PremiumUser = {
    id: 2,
    name: "Jane Smith",
    email: "jane@example.com",
    joinedDate: new Date("2024-03-20")
    // membershipLevel is omitted - that's fine, it's optional
};

printUserDetails(regularPremium);
// Output shows Gold membership

printUserDetails(freeUser);
// Output shows "Standard (Free)" for membership

// Attempting to modify readonly properties:
// regularPremium.id = 999; // Error: Cannot assign to 'id' because it is a read-only property
// regularPremium.joinedDate = new Date(); // Error: joinedDate is also readonly