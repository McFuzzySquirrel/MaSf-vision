# User Personas

## Overview

This document defines the key user personas for the MaS platform, helping guide design and development decisions.

## Primary Personas

### Persona 1: Remote Rural Learner

**Name**: Sarah  
**Age**: 14  
**Location**: Rural village, limited infrastructure  
**Device**: 3-year-old Android phone (2GB RAM)  
**Connectivity**: Mobile data available 2-3 times per week in town  

#### Background
- Attends local school with limited resources
- Walks 2km to school each day
- Shares phone with siblings
- Family income is limited
- Very motivated to learn

#### Goals
- Complete secondary education
- Learn at own pace
- Access quality educational content
- Track progress and achievements
- Prepare for exams

#### Pain Points
- No internet at home
- Limited study materials
- Few qualified teachers
- Power outages common
- Limited device storage

#### Use Cases
- Downloads content packages weekly when in town
- Studies offline at home in evenings
- Completes assessments independently
- Syncs progress when connectivity available
- Shares content with classmates via Bluetooth

#### Success Criteria
- Can access all content offline
- Fast app performance on old device
- Minimal data usage for sync
- Clear progress tracking
- Works reliably without crashes

---

### Persona 2: Urban Self-Learner

**Name**: Ahmad  
**Age**: 22  
**Location**: Urban area, shared apartment  
**Device**: Mid-range smartphone  
**Connectivity**: WiFi at work, mobile data  

#### Background
- Works full-time in retail
- Wants to improve job skills
- Studies in spare time
- Limited formal education
- Self-motivated and disciplined

#### Goals
- Learn new skills (IT, business, languages)
- Earn certificates
- Improve career prospects
- Study during commute
- Flexible learning schedule

#### Pain Points
- Limited time for studying
- Cannot afford traditional courses
- Needs proof of learning
- Distracted by other apps
- Inconsistent study habits

#### Use Cases
- Studies during commute (30 min each way)
- Reviews content during breaks
- Completes assessments to earn badges
- Tracks progress toward certificates
- Uses offline mode when data is limited

#### Success Criteria
- Quick access to resume learning
- Progress synced across sessions
- Engaging content that holds attention
- Clear skill progression
- Recognized certifications

---

### Persona 3: Classroom Teacher

**Name**: Mrs. Okafor  
**Age**: 38  
**Location**: Semi-urban school  
**Device**: Personal smartphone, school tablet  
**Connectivity**: WiFi at school, mobile data  

#### Background
- 15 years teaching experience
- Class of 35 students
- Limited teaching resources
- Some technology experience
- Dedicated but overworked

#### Goals
- Improve student learning outcomes
- Reduce administrative burden
- Monitor student progress
- Assign and review homework
- Differentiate instruction

#### Pain Points
- Too many students per class
- Limited time to track individual progress
- Difficult to distribute materials
- Cannot help all students individually
- Hard to assess understanding

#### Use Cases
- Assigns content to entire class
- Monitors completion and scores via edge device
- Identifies struggling students
- Provides targeted help
- Generates progress reports

#### Success Criteria
- Easy content assignment
- Clear progress dashboard
- Works with minimal setup
- Reliable in classroom environment
- Minimal time investment

---

## Secondary Personas

### Persona 4: School Administrator

**Name**: Mr. Patel  
**Age**: 45  
**Role**: School Principal  
**Focus**: Implementation, oversight, reporting  

#### Goals
- Improve school outcomes
- Justify technology investment
- Monitor teacher and student engagement
- Report to district/board
- Manage resources efficiently

#### Use Cases
- Reviews school-wide analytics
- Manages teacher accounts
- Allocates content licenses
- Generates reports for stakeholders
- Plans technology rollout

---

### Persona 5: Content Creator

**Name**: Dr. Chen  
**Age**: 52  
**Role**: Education content specialist  
**Focus**: Creating quality learning materials  

#### Goals
- Create engaging educational content
- Reach underserved learners
- Publish content easily
- Track content effectiveness
- Iterate based on feedback

#### Use Cases
- Creates lessons using content tools
- Packages content for distribution
- Reviews learning analytics
- Updates content based on feedback
- Publishes to content library

---

### Persona 6: Parent/Guardian

**Name**: Maria  
**Age**: 35  
**Role**: Parent of two students  
**Focus**: Supporting children's education  

#### Goals
- Monitor children's progress
- Support learning at home
- Ensure appropriate content
- Justify screen time
- Encourage consistent study

#### Use Cases
- Reviews children's progress
- Sets study time limits
- Receives notifications of achievements
- Discusses learning with children
- Coordinates with teachers

---

## Anti-Personas

### Who We're NOT Building For

#### The Enterprise Learner
- Works in corporate environment
- Has high-end devices and reliable connectivity
- Expects LMS integration
- Needs compliance tracking

*Why*: Our focus is resource-constrained environments, not corporate training.

#### The Early Childhood Learner (< 8 years)
- Needs highly interactive content
- Limited reading ability
- Requires adult supervision
- Different pedagogical approach

*Why*: Initial focus is on older learners who can study independently.

## Persona Usage

### In Design
- Reference personas in design reviews
- Test designs against persona needs
- Prioritize features for primary personas
- Ensure accessibility for all personas

### In Development
- Consider constraints of each persona
- Test on devices personas would use
- Validate use cases work as expected
- Measure against persona success criteria

### In Content
- Create content appropriate for age/level
- Consider context of use
- Support different learning styles
- Provide clear progression paths

## Related Documents

- [Vision](vision.md)
- [Constraints](constraints.md)
- [Success Metrics](success-metrics.md)
