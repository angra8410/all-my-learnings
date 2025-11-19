# Instructor Notes - AI-Powered Workflows Bootcamp

## 📚 Course Overview

This 16-week bootcamp teaches practical AI development skills with a focus on production-ready applications. The course follows the Pareto Principle (80/20 rule) with 80% hands-on practice and 20% theory.

## ⏱️ Time Allocation Recommendations

### Weekly Structure (4-5 hours per week)
- **Theory & Concepts** (45-60 min): Review README.md
- **Hands-on Exercises** (2-3 hours): Work through actividad-interactiva.md
- **Capstone Integration** (45-60 min): Complete project-steps.md
- **Review & Reflection** (30 min): Update progreso.md and review

### Live Session Recommendations (if applicable)
- **Week Kickoff** (30 min): Overview of concepts, Q&A from previous week
- **Mid-week Office Hours** (60 min): Help with exercises, debugging
- **Week Wrap-up** (30 min): Review key learnings, preview next week

## 🎯 Teaching Philosophy

### Pareto Principle Application
The course is designed around the 20/80 rule:
- **20% of Concepts**: Core fundamentals that unlock 80% of practical value
- **80% of Practice**: Hands-on application, building real projects

### Project-First Approach
- Every week connects to capstone projects
- Incremental building towards 4 complete applications
- Students create a portfolio by course end

## 📋 Week-by-Week Guidance

### Weeks 0-4: Foundations
**Focus**: Environment, prompts, RAG basics, Python for AI

**Teaching Tips**:
- Week 00 is critical - ensure all students have working environments
- Week 01 (Prompts) - emphasize iteration and measurement
- Week 02 (RAG) - introduce vector databases hands-on
- Week 04 - focus on practical Python patterns, not advanced theory

**Common Issues**:
- API key configuration problems (Week 00)
- Understanding embeddings conceptually (Week 02)
- Async I/O confusion (Week 04)

**Office Hour Topics**:
- Environment troubleshooting
- Prompt engineering practice
- Vector database setup

### Weeks 5-8: Advanced Techniques
**Focus**: Agents, fine-tuning, evaluation

**Teaching Tips**:
- Week 05-06 (Agents) - start simple, build complexity
- Week 07 (Fine-tuning) - emphasize when NOT to fine-tune
- Week 08 (Evaluation) - metrics matter, teach measurement

**Common Issues**:
- Agent complexity overwhelming students
- Fine-tuning expectations vs reality
- Evaluation metric selection

**Office Hour Topics**:
- Agent design patterns
- When to fine-tune vs prompt engineer
- Choosing right evaluation metrics

### Weeks 9-13: Production & Operations
**Focus**: Testing, security, ethics, orchestration

**Teaching Tips**:
- Week 10 (Security) - make it practical, not theoretical
- Week 11 (Ethics) - discuss real cases, encourage critical thinking
- Week 13 (Orchestration) - focus on CI/CD for ML

**Common Issues**:
- Security concerns feeling overwhelming
- Ethics discussions becoming abstract
- Orchestration tool complexity

**Office Hour Topics**:
- Practical security implementation
- Ethics case studies
- CI/CD setup for AI projects

### Weeks 14-16: Capstone Projects
**Focus**: Real-world applications

**Teaching Tips**:
- These weeks are project-intensive
- Encourage code reuse from previous weeks
- Group code reviews are valuable
- Final presentations should be professional

**Common Issues**:
- Scope creep in capstone projects
- Integration challenges
- Time management

**Office Hour Topics**:
- Project scoping and prioritization
- Integration debugging
- Presentation preparation

## 🎓 Assessment Guidance

### Weekly Deliverables (60% of final grade)
**Grading Criteria**:
- Correctness (60%): Does it work? Does it solve the problem?
- Reproducibility (20%): Can another person run it?
- Documentation (20%): Is it well-documented and clear?

**Quick Grading Tips**:
- Use provided rubrics in retroalimentacion.md
- Focus on learning progress, not perfection
- Partial credit for incomplete but thoughtful work
- Encourage iteration and improvement

### Capstone Projects (40% of final grade)
**Grading Breakdown**:
- Functionality & Reproducibility: 40%
- Modeling & Prompt Quality: 25%
- Testing & Monitoring: 15%
- Ethics & Security: 10%
- Documentation & Demo: 10%

**Evaluation Tips**:
- Test running the code yourself
- Review security practices carefully
- Check for proper error handling
- Assess code organization and documentation

## 💡 Best Practices for Instructors

### Before the Course
1. **Complete Week 00 yourself** - understand setup challenges
2. **Prepare environment troubleshooting guide** - common issues
3. **Set up communication channels** - Discord/Slack/email
4. **Review capstone projects** - understand scope and requirements

### During the Course
1. **Check in weekly** - monitor student progress
2. **Provide timely feedback** - within 3-5 days of submission
3. **Share examples** - showcase good student work (with permission)
4. **Be available** - hold regular office hours

### Feedback Tips
1. **Be specific**: Not "good work" but "your prompt engineering in Exercise 3 showed excellent use of few-shot learning"
2. **Be constructive**: Point out improvements with actionable advice
3. **Encourage growth**: Acknowledge progress from previous weeks
4. **Highlight strengths**: Everyone has something they're doing well

## 🚨 Common Student Challenges

### Technical Challenges
1. **API costs**: Remind students to set usage limits
2. **Environment issues**: Most common in Week 00
3. **Git confusion**: Basic git commands need reinforcement
4. **Docker problems**: Optional but students may struggle

**Solutions**:
- Provide debugging guides
- Create FAQ document
- Hold troubleshooting sessions
- Pair students for peer support

### Learning Challenges
1. **Pace too fast**: Some students need more time
2. **Concepts unclear**: Abstract AI concepts need concrete examples
3. **Overwhelm**: Too many tools/frameworks
4. **Integration confusion**: How pieces fit together

**Solutions**:
- Offer extension options when appropriate
- Use more examples and analogies
- Create "tools cheat sheet"
- Draw architecture diagrams

### Project Challenges
1. **Scope management**: Students bite off too much
2. **Time management**: Underestimate effort
3. **Technical debt**: Quick hacks accumulate
4. **Integration issues**: Components don't work together

**Solutions**:
- Help scope projects early
- Teach estimation and planning
- Encourage refactoring
- Review architecture before building

## 📊 Success Metrics

### Course-Level Metrics
- **Completion rate**: Target 70%+
- **Average grade**: Target 75%+
- **Capstone completion**: Target 85%+
- **Student satisfaction**: Track via surveys

### Individual Student Metrics
- Week-by-week progress
- Exercise completion rates
- Code quality improvement over time
- Engagement in office hours/discussions

## 🔧 Tools & Resources for Instructors

### Recommended Tools
- **GitHub**: Code review and version control
- **Discord/Slack**: Communication
- **Google Classroom/Canvas**: Assignment submission
- **Calendly**: Office hour scheduling
- **Loom**: Video feedback on code

### Time-Saving Tips
1. **Reuse rubrics**: Use provided evaluation templates
2. **Batch grading**: Grade similar exercises together
3. **Video feedback**: Faster than written for complex issues
4. **Student showcases**: Learn from each other
5. **Auto-testing**: Where possible, automate checks

## 📅 Suggested Calendar

### 16-Week Schedule
```
Week 00: Setup         → Week 04: Python for AI
Week 01: Prompts       → Week 05: Agents & Tools  
Week 02: RAG           → Week 06: Agentic AI
Week 03: Workflows     → Week 07: Fine-tuning

Week 08: Evaluation    → Week 12: Automation
Week 09: Testing       → Week 13: Orchestration
Week 10: Security      → Week 14: Finance Case
Week 11: Ethics        → Week 15: Sports Case

Week 16: E-commerce + Enterprise + Final Presentations
```

### Milestone Checkpoints
- **Week 4**: Foundations complete, first capstone components
- **Week 8**: Advanced techniques learned, capstone 50% done
- **Week 13**: Production skills acquired, capstone 80% done
- **Week 16**: All capstones complete, final presentations

## 💬 Communication Templates

### Week Kickoff Email
```
Subject: Week [X]: [Title] - Let's Get Started!

Hi everyone,

This week we're covering [topic]. Here's what to expect:

📚 Key Concepts: [brief list]
⏰ Time Commitment: 4-5 hours
🎯 Main Deliverables: [list]

Office Hours: [time and link]
Questions: Post in #week-[X] channel

Let's have a great week!
[Your name]
```

### Feedback Template
```
Hi [Student],

Great work on Week [X]! Here's your feedback:

✅ Strengths:
- [specific positive feedback]

📈 Areas for Improvement:
- [specific, actionable feedback]

Grade: [X]/100
Next Steps: [what to focus on]

Keep up the good work!
[Your name]
```

## 🎯 FAQ for Instructors

**Q: Student is falling behind. What should I do?**
A: Reach out personally, understand blockers, offer extensions if needed, connect with peer for support

**Q: How strict should grading be?**
A: Focus on learning progress. 70% is passing. Be fair but encourage growth

**Q: Student's code doesn't run. How to grade?**
A: Partial credit for attempt and understanding. Require resubmission with working code

**Q: How to handle AI-generated code submissions?**
A: Clarify policies upfront. Focus on understanding - require explanation of code

**Q: What if a student wants to go deeper?**
A: Excellent! Point to "Further Reading" sections, suggest bonus projects

## 🌟 Tips for Success

1. **Be enthusiastic**: Your energy affects student engagement
2. **Be available**: Students need support, especially early weeks
3. **Be flexible**: Not all students learn at same pace
4. **Be practical**: Focus on what works in production
5. **Be encouraging**: AI is complex - celebrate progress

## 📝 End of Course Checklist

- [ ] All weeks graded and feedback provided
- [ ] Capstone projects evaluated
- [ ] Final grades calculated
- [ ] Course survey sent to students
- [ ] Certificate/completion documentation prepared
- [ ] Follow-up resources shared
- [ ] Student showcase organized (optional)

---

## 🎓 Final Thoughts

This course is designed to be practical and project-focused. The goal is for students to leave with:

✅ 4 production-ready AI applications in their portfolio
✅ Deep understanding of AI workflows
✅ Confidence to build and deploy AI systems
✅ Network of peers and community

Success is measured not just by grades, but by what students can build and deploy after the course.

**Good luck, and enjoy teaching! 🚀**

---

**Questions or Feedback?** This is a living document. Improve it as you learn what works best for your students.
