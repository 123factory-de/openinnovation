# Pull Request Convention

To ensure high-quality code reviews and a clear project history, all Pull Requests (PRs) should follow this convention.

## PR Title Format
Follow the same convention as our commit messages:
`<type>[optional scope]: <description>`

Examples:
- `feat: add contact form section`
- `fix: resolve mobile responsiveness in footer`
- `docs: update PR convention document`

## PR Description Template
A good PR description helps reviewers understand **what** changed and **why**.

```markdown
## Summary
Briefly describe the changes introduced by this PR.

## Key Changes
- List major technical changes or architectural decisions.
- Mention any new dependencies added.

## Related Issues
- Closes #123 (if applicable)

## Screenshots / Media (Optional)
Add screenshots or videos for UI-related changes or proof of functionality.

## Checklist
- [ ] My code follows the project's style guidelines.
- [ ] I have performed a self-review of my code.
- [ ] I have commented my code, particularly in hard-to-understand areas.
- [ ] My changes generate no new warnings.
```

## PR Process
1. **Atomic PRs**: Keep PRs focused on a single task or feature.
2. **Draft PRs**: Use Draft PRs for work-in-progress if you need early feedback.
3. **Reviewers**: Tag relevant team members for review.
4. **Approval**: At least one approval is required before merging into `main` (for team projects).
