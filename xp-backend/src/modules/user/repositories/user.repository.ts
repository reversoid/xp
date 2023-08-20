import { Injectable } from '@nestjs/common';
import { DataSource, Repository } from 'typeorm';
import { User } from '../entities/user.entity';

@Injectable()
export class UserRepository extends Repository<User> {
  constructor(dataSource: DataSource) {
    super(User, dataSource.createEntityManager());
  }

  getUserByUsername(username: string) {
    return this.findOneBy({ username: username });
  }

  editUsername(userId: number, username: string) {
    return this.save({ id: userId, username });
  }
}
