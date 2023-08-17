import { ApiProperty } from '@nestjs/swagger';

export class IsRegisteredByTgId {
  @ApiProperty()
  registered: boolean;
}
