# PHP Upgrade

### Lab Goal

The idea is to practice updating software that has multiple versions available in the repos using the yum replace plugin. This can make upgrading/updating software versions easy but can have pitfalls when upgrading/downgrading an packages become deprecated.

### Usage Example

```
$ yum replace php --replace-with=php56U
```