
# RWS SPARK QA Assessment – Test Design Document

## 1. Tool & Application

- **Automation Tool**: Selenium WebDriver with Python
- **Test Framework**: pytest
- **Design Pattern**: Page Object Model (POM)
- **Application Under Test (AUT)**: [SauceDemo](https://www.saucedemo.com)
- **Browser**: Google Chrome (latest stable)

---

## 2. Test Scope

**In Scope**:
- Login flow
- Product listing page
- Cart functionality
- Checkout process

**Out of Scope**:
- Backend services
- Performance or load testing
- Mobile view/responsiveness

---

## 3. Test Types

- Functional UI Testing
- Positive & Negative Testing
- Boundary Value Analysis (BVA)
- Edge Case Testing
- End-to-End Scenario Testing

---

## 4. Assumptions & Environment

- The site is publicly accessible.
- The demo credentials are stable.
- Network latency is minimal and consistent.
- Tests run on Chrome (locally or via CI).

---

## 5. Test Strategy

- Use Page Object Model (POM) for test code modularity and scalability.
- Maintain logical grouping in page classes.
- Base test setup/teardown via pytest fixtures.
- Use implicit waits and proper error handling.

---

## 6. Test Case Matrix

| TC ID | Title | Type | Inputs / Conditions | Expected Result |
|-------|-------|------|----------------------|------------------|
| TC01 | Valid Login | Positive | `standard_user` / `secret_sauce` | Redirect to `/inventory.html` |
| TC02 | Invalid Login | Negative | Invalid username | Error message shown |
| TC03 | Invalid Login | Negative | Invalid password | Error message shown |
| TC04 | Empty Fields | Negative | Leave both fields blank | Error shown |
| TC05 | Username Max Length | BVA | 50-character input | Accepted or rejected properly |
| TC06 | Sort Inventory Page by Name in Increasing Order | Positive | Click Sort | Inventory page updates |
| TC07 | Sort Inventory Page by Name in Decreasing Order | Positive | Click Sort | Inventory page updates |
| TC08 | Sort Inventory Page by Price in Increasing Order | Positive | Click Sort | Inventory page updates |
| TC09 | Sort Inventory Page by Price in Decreasing Order | Positive | Click Sort | Inventory page updates |
| TC10 | Add to Cart | Positive | Click Add to Cart on one item | Cart updates |
| TC11 | Remove from Cart | Positive | Remove item | Cart updates |
| TC12 | Cart Persistence | Edge | Add → Refresh | Cart retains item |
| TC13 | Checkout without First Name | Negative | Click Checkout without First name | Error message shown |
| TC14 | Checkout without Last Name | Negative | Click Checkout without Last name | Error message shown |
| TC15 | Checkout without Zip Code | Negative | Click Checkout without Zip Code | Error message shown |
| TC16 | Invalid ZIP | Negative | Letters in ZIP | Error shown |
| TC17 | Successful Checkout | Positive | Complete flow with valid input | Confirmation message |
| TC18 | Logout | Positive | Logout from menu | Redirect to login page |

---

## 7. Boundary, Edge & Negative Highlights

**Boundary Cases**:
- Max Username/Password length
- Max field length in checkout (100–200 chars)
- ZIP edge cases: "00000", "99999", "ABCDE"

**Negative Cases**:
- Invalid login
- Empty or bad-formatted input
- Checkout without adding to cart

**Edge Cases**:
- Refreshing during checkout
- Adding all products
- Performing actions from multiple tabs

---

## 8. Justification for Selected Automated Tests

### ✅ TC01 – Valid Login
- Ensures authentication works.
- If broken, entire app is unusable.

### ✅ TC17 – Successful Checkout
- Tests revenue-driving flow.
- Verifies end-to-end user journey.
- Includes cart, form fill, and order completion.

---

## 9. Final Notes

- Tests are built using scalable page classes.
- Logging and error reporting can be added.
- Easily extendable for CI integration (GitHub Actions / Jenkins).

---
