import { ApiProperty } from '@nestjs/swagger';
import { User } from 'src/modules/user/entities/user.entity';

export class UserResponse implements Partial<User> {
  @ApiProperty()
  id: number;

  @ApiProperty()
  tg_id: number;

  @ApiProperty()
  username: string;
}
